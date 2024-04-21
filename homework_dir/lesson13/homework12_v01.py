""" Homework 12. OOP-2 """
from abc import ABC, abstractmethod
from pathlib import Path

print("-"*10 + "Task1" + "-"*10)


class AbstractDevice(ABC):
    """
    An abstract class that represents a generic device for operations such as turning on and off
    """

    @abstractmethod
    def turn_on(self):
        """Abstract method to turn on the device that must be implemented by any subclass."""
        pass

    @abstractmethod
    def turn_off(self):
        """Abstract method to turn off the device that must be implemented by any subclass."""
        pass


class ConcreteDevice(AbstractDevice):
    """
    Concrete implementation of AbstractDevice with its abstract methods.
    """

    def turn_on(self):
        """Implements the turn_on method to activate the device."""
        print("Device is now ON.")

    def turn_off(self):
        """Implements the turn_off method to deactivate the device."""
        print("Device is now OFF.")


# Example usage
if __name__ == "__main__":
    device = ConcreteDevice()
    device.turn_on()
    device.turn_off()

print("\n" + "-"*10 + "Task2" + "-"*10)


class TV:
    """Class to represent a Television set with basic operations."""
    def __init__(self, type: str):
        self.type = type

    def turn_on(self):
        print(f"{self.type} TV is turned on.")

    def turn_off(self):
        print(f"{self.type} TV is turned off.")


class Lights:
    """Class to represent Home Lighting system with basic operations."""
    def __init__(self, location: str):
        self.location = location

    def turn_on(self):
        print(f"{self.location} lights are turned on.")

    def turn_off(self):
        print(f"{self.location} lights are turned off.")


class Heating:
    """Class to represent Heating system with basic operations."""
    def __init__(self, type: str, temperature: float):
        self.type = type
        self.temperature = temperature

    def turn_on(self):
        print(f"Heating on at {self.temperature}°C for {self.type} heating.")

    def turn_off(self):
        print(f"Heating off for {self.type} heating.")

    def set_temperature(self, temperature: float):
        self.temperature = temperature
        print(f"Temperature set to {self.temperature}°C for {self.type} heating.")


class HomeFacade:
    """
    Facade class to manage different systems through a simplified interface.
    """
    def __init__(self, tv_type: str, light_location: str, heating_type: str, temperature: float):
        self.__tv = TV(tv_type)
        self.__lights = Lights(light_location)
        self.__heating = Heating(heating_type, temperature)

    @property
    def tv(self):
        return self.__tv

    @property
    def lights(self):
        return self.__lights

    @property
    def heating(self):
        return self.__heating

    def come_home(self):
        """Method to turn on necessary systems when coming home."""
        print("Coming home...")
        self.lights.turn_on()
        self.heating.turn_on()
        self.tv.turn_on()

    def go_out(self):
        """Method to turn off all systems when going out."""
        print("Going out...")
        self.heating.turn_off()
        self.tv.turn_off()
        self.lights.turn_off()

    def go_to_sleep(self, temperature: float):
        """Method to prepare all systems for sleep."""
        self.heating.set_temperature(temperature)
        self.lights.turn_off()
        self.tv.turn_off()


# Example usage
if __name__ == "__main__":
    home1 = HomeFacade("Samsung", "Living room", "Central Gas Heating", 45)
    home1.come_home()
    home1.go_out()

    home2 = HomeFacade(tv_type="LG", light_location="Kitchen", heating_type="Electric", temperature=40)
    home2.come_home()
    home2.go_to_sleep(35)

print("\n" + "-"*10 + "Task3" + "-"*10)


class MyContextManager:
    """
    A custom context manager to simplify opening and closing files within a specific folder.
    """

    def __init__(self, filename: str, mode: str, directory='test_folder'):
        self.directory = Path(directory)
        self.filename = filename
        self.mode = mode
        self.file = None
        self.full_path = self.directory.joinpath(self.filename)
        self.directory.mkdir(parents=True, exist_ok=True)

    def __enter__(self):
        """Open the file in the specified mode."""
        self.file = self.full_path.open(mode=self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Ensure the file is closed when the block using the context manager ends."""
        if self.file:
            self.file.close()
        # Handle exceptions if necessary
        if exc_type is not None:
            print(f"Exception occurred: {exc_type}, {exc_val}")
        # Return False to propagate exceptions, True to suppress them
        return False


# Example usage
if __name__ == "__main__":
    with MyContextManager('example.txt', 'w') as file:
        file.write("Hello, this is a test file.\n")
        file.write("This file was managed by my custom context manager.\n")

    print("File has been written in the specified folder and closed.")

try:
    with MyContextManager('example.txt', 'r'):
        print("Inside the context manager block.")
        raise ValueError("Something went wrong!")  # Deliberately raising an exception
except ValueError as e:
    print(f"Caught an exception outside the context manager: {str(e)}")
