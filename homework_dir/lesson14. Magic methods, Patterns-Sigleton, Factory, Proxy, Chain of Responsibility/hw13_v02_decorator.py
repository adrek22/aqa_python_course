""" Homework 13. Pattern: Singleton using decorator """


def singleton(cls):
    """
    A decorator that modifies a class to behave as a Singleton.
    This ensures that only one instance of the class exists.
    """
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            # Instantiate the class if an instance doesn't exist
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class ConfigurationManager:
    """
    Configuration manager for an application that uses the singleton pattern.
    This class manages configuration settings for the application.
    """

    def __init__(self):
        self.config = {}

    def set_config(self, key, value):
        """Set a configuration value."""
        self.config[key] = value

    def get_config(self, key):
        """Get a configuration value."""
        return self.config.get(key)


# Example Usage
if __name__ == "__main__":
    # Set configuration
    config_manager = ConfigurationManager()
    config_manager.set_config('theme', 'dark')

    # Retrieve configuration from another instance
    new_config_manager = ConfigurationManager()
    print(f"Theme: {new_config_manager.get_config('theme')}")

    # Check if both instances are the same
    print(f"Are both instances the same? {'Yes' if config_manager is new_config_manager else 'No'}")
