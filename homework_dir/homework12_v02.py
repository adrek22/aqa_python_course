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
        if self.check_for_empty_str(value):
            self._name = value
        else:
            raise ValueError("Course name cannot be empty.")

    @property
    def instructor(self):
        """Gets the instructor's name."""
        return self._instructor

    @instructor.setter
    def instructor(self, value: str):
        """Sets the instructor's name."""
        if self.check_for_empty_str(value):
            self._instructor = value
        else:
            raise ValueError("Instructor name cannot be empty.")

    @property
    def duration(self):
        """Gets the course's duration in weeks."""
        return self._duration

    @duration.setter
    def duration(self, value: int):
        """Sets the course's duration in weeks"""
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Duration must be a positive integer.")
        self._duration = value

    def display_course_details(self):
        """Outputs the details of a course."""
        print(f"Course Name: {self.name}")
        print(f"Instructor: {self.instructor}")
        print(f"Duration: {self.duration} weeks")

    @staticmethod
    def check_for_empty_str(text: str):
        if text.strip():
            return True

    @classmethod
    def print_total_number_of_courses(cls):
        print(f"Total courses available: {cls.total_courses}")


class Workshop(Course):
    """Subclass of Course designed for practical, location-based learning sessions.

    Attributes:
        name (str): Name of the workshop.
        instructor (str): Instructor's name.
        duration (int): Duration in hours.
        location (str): Venue of the workshop.
        materials (list of str): Required materials for the workshop.
    """
    def __init__(self, name: str, instructor: str, duration: int, location: str, materials: list):
        super().__init__(name, instructor, duration)
        self.location = location
        self.materials = materials

    def display_workshop_details(self):
        """Outputs the location and list of materials required for the workshop."""
        self.display_course_details()
        print(f"Workshop Location: {self.location}")
        print(f"Materials Needed: {self.materials}")


# Create instances of Course
qa_manual_course = Course(name="QA Manual", instructor="Olena Kovalenko", duration=6)
qa_technical_pro_course = Course(name="QA Technical Pro", instructor="Dmytro Petrov", duration=12)
qa_auto_python_course = Course(name="QA Automation — Python", instructor="Viktor Melnyk", duration=8)

# Check the number of courses created
Course.print_total_number_of_courses()

# Display details of the courses
qa_manual_course.display_course_details()

# Test validation on empty name
try:
    qa_manual_course.name = ""
except ValueError as e:
    print(e)

# Create an instance of the Workshop subclass
data_science_workshop = Workshop(
    name="Data Science Fundamentals",
    instructor="Mariia Ivanova",
    duration=3,
    location="Kyiv National Library",
    materials=["Laptop", "Notebook", "DataCamp Subscription"]
)

# Display workshop details
data_science_workshop.display_workshop_details()

# Test validation for duration
try:
    data_science_workshop.duration = -5
except ValueError as e:
    print(e)

# Check the final number of courses
Course.print_total_number_of_courses()
