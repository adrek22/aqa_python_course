import sys
import allure

from functools import wraps
from allure_commons.types import AttachmentType
from homework_dir.lesson19_selenium2.hw15.driver import shared_driver


def step(step_title: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """
            :param soft: type: str, Its logic controller that solve is step soft or not
            :param catcher: type: ErrCatcher, Its instance that collect assertions
            :return: func
            """
            if kwargs.get('soft') and kwargs.get('catcher'):
                catcher = kwargs.get('catcher')
                try:
                    with allure.step(step_title):
                        return func(*args, **kwargs)
                except AssertionError:
                    allure.attach(shared_driver.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
                    exception_msg = '\n\n' + 'Step title: ' + step_title + '\n' + form_exception_message()
                    catcher.get_result(exception_msg=exception_msg)
            else:
                with allure.step(step_title):
                    return func(*args, **kwargs)

        return wrapper

    return decorator


class ErrCatcher:

    def __init__(self):
        self._errors = []

    def get_result(self, exception_msg: str) -> None:
        self._errors.append(exception_msg)

    def has_errors(self):
        assert len(self._errors) == 0, self.__str__()

    def __str__(self):
        return '\n'.join(self._errors)


def form_exception_message():
    exception_type, exception_object, exception_traceback = sys.exc_info()
    return exception_object.__str__()
