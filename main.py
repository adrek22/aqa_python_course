# main module code if available
from pathlib import Path


def create_lesson_folders(base_path, start=1, end=32):
    """
    Creates a series of folders named 'lessonX' within a given base path,
    where X ranges from start to end. Skips folder creation if it already exists.

    Args:
    - base_path (str): The base directory in which to create lesson folders.
    - start (int): The starting lesson number (inclusive).
    - end (int): The ending lesson number (inclusive).
    """
    base_directory = Path(base_path)
    for i in range(start, end + 1):
        lesson_folder = base_directory / f'lesson{i}. '
        if not lesson_folder.exists():
            lesson_folder.mkdir(parents=True, exist_ok=True)
            print(f"Created folder: {lesson_folder}")
        else:
            print(f"Folder already exists: {lesson_folder}")


# Specify the path for folder creation
base_path = r'C:\Users\mmaznyk\PycharmProjects\aqa_python_course_personal\homework_dir'
create_lesson_folders(base_path)
