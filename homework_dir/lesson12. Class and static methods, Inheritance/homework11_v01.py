""" Homework 12. OOP """


class Course:
    """Represents a course in the program.

    Attributes:
        total_courses (int): Class attribute to count the total number of courses.
        name (str): The name of the course.
        instructor (str): The instructor's name.
        duration (int): The duration of the course in weeks.
    """

    total_courses = 0

    def __init__(self, name: str, instructor: str, duration: int):
        self._name = name
        self._instructor = instructor
        self._duration = duration
        Course.total_courses += 1

    @property
    def name(self):
        """Gets the course's name."""
        return self._name

    @name.setter
    def name(self, value: str):
        """Sets the course's name."""
        self._name = value

    @property
    def instructor(self):
        """Gets the instructor's name."""
        return self._instructor

    @instructor.setter
    def instructor(self, value: str):
        """Sets the instructor's name."""
        self._instructor = value

    @property
    def duration(self):
        """Gets the course's duration in weeks."""
        return self._duration

    @duration.setter
    def duration(self, value: int):
        """Sets the course's duration in weeks"""
        self._duration = value

    @classmethod
    def print_total_number_of_courses(cls):
        print(f"Total courses available: {cls.total_courses}")


class Student(Course):
    """Represents a student enrolled in courses within the program.

    Attributes:
        name (str): The student's name.
        email (str): The student's email.
        enrolled_courses (list): A list of courses the student is enrolled in.
    """

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.enrolled_courses = []

    def enroll(self, course):
        """Enrolls the student in a new course.

        Args:
            course (Course): The course to enroll in.
        """
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            print(f"{self.name} has been enrolled in {course.name} with {course.instructor} as instructor that lasts "
                  f"{course.duration} weeks.")
        else:
            print(f"{self.name} is already enrolled in {course.name}.")

    def list_courses(self):
        """Lists all courses the student is enrolled in."""
        if self.enrolled_courses:
            courses = ', '.join(course.name for course in self.enrolled_courses)
            print(f"{self.name} with email:{self.email} is enrolled in the following courses: {courses}")
        else:
            print(f"{self.name} with email:{self.email} is not enrolled in any courses.")


# Create instances of Course
qa_manual_course = Course(name="", instructor="", duration=0)
qa_manual_course.name = "QA Manual"
qa_manual_course.instructor = "Olena Kovalenko"
qa_manual_course.duration = 0
qa_technical_pro_course = Course(name="QA Technical Pro", instructor="Dmytro Petrov", duration=12)
qa_auto_java_course = Course(name="QA Automation — Java", instructor="Iryna Shevchenko", duration=10)
qa_auto_python_course = Course(name="QA Automation — Python", instructor="Viktor Melnyk", duration=8)
qa_auto_javascript_course = Course(name="QA Automation — JavaScript", instructor="Anastasiia Bondarenko", duration=8)
qa_auto_csharp_course = Course(name="QA Automation — C#", instructor="Yurii Zahorodnii", duration=9)
python_for_beginners_course = Course(name="Python for Beginners", instructor="Kateryna Horova", duration=8)

# Print total courses for verification
Course.print_total_number_of_courses()

# Create instances of Student
student1 = Student(name="Oleksii Morozov", email="oleksii.morozov@example.com")
student2 = Student(name="Mariia Ivanova", email="mariia.ivanova@example.com")
student3 = Student(name="Vladyslav Kozak", email="vladyslav.kozak@example.com")
student4 = Student(name="Mykhailo Vozniak", email="mykhailo.vozniak@example.com")

# Enroll students in courses
student1.enroll(qa_manual_course)
student2.enroll(qa_technical_pro_course)
student3.enroll(qa_auto_java_course)
student1.enroll(qa_auto_python_course)
student2.enroll(qa_auto_javascript_course)
student3.enroll(qa_auto_csharp_course)
student1.enroll(python_for_beginners_course)
student1.enroll(python_for_beginners_course)

# List courses each student is enrolled in
student1.list_courses()
student2.list_courses()
student3.list_courses()
student4.list_courses()
