import requests
from requests import Response
from typing import Optional
from homework_dir.lesson24_api_regex.hm16 import config
from http.client import HTTPException

from functools import wraps


def api_dec(func):
    @wraps(func)
    def inner(*args, **kwargs):
        max_attempts = 2
        for attempt in range(max_attempts):
            res: Response = func(*args, **kwargs)
            status_code = res.status_code
            if status_code in (200, 201, 204):
                print(f"{func.__name__} is executed successfully")
                return res
            if attempt < max_attempts - 1:
                continue
            if not kwargs.get('negative_flow'):
                endpoint = "".join([arg for arg in args if isinstance(arg, str)])
                raise HTTPException(
                    f"Request failed with status code {status_code} to {endpoint}, "
                    f"response: {res.text}, reason: {res.reason}"
                )
        return res

    return inner


class APIInterface:
    def __init__(self):
        self.headers = {
            'Content-Type': 'application/json',
        }

    @api_dec
    def _get(self, endpoint: str, params=None, **kwargs) -> Response:
        """Send a GET request to the specified endpoint."""
        return requests.get(config.api.url + endpoint, headers=self.headers, params=params)

    @api_dec
    def _post(self, endpoint: str, json=None, files: dict = None, data: dict = None, timeout: int = 10, **kwargs) -> Response:
        """Send a POST request to the specified endpoint."""
        return requests.post(config.api.url + endpoint, json=json, data=data, headers=self.headers, files=files,
                             timeout=timeout)

    @api_dec
    def _put(self, endpoint: str, body=None, **kwargs) -> Response:
        """Send a PUT request to the specified endpoint."""
        return requests.put(config.api.url + endpoint, json=body, headers=self.headers)

    @api_dec
    def _delete(self, endpoint: str, params: Optional[dict] = None, body=None, **kwargs) -> Response:
        """Send a DELETE request to the specified endpoint."""
        return requests.delete(config.api.url + endpoint, json=body, headers=self.headers, params=params)
