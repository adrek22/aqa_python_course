""" Homework 13. Pattern: Singleton using metaclass """


class SingletonMeta(type):
    """
    A Singleton metaclass that creates only one instance for any class that uses this metaclass.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            # Create a new instance if one doesn't exist
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Database(metaclass=SingletonMeta):
    """
    Example class using the SingletonMeta metaclass. This class simulates a database connection.
    """
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def connect(self):
        print(f"Connecting to the database at {self.connection_string}")


# Example Usage
if __name__ == "__main__":
    # Create first instance
    db1 = Database("Server=host1;Port=1234;User=user1;Password=secret1")
    db1.connect()

    # Try to create a second "different" instance
    db2 = Database("Server=host2;Port=4321;User=user2;Password=secret2")
    db2.connect()

    # Check if both instances are indeed the same
    print(f"db1 and db2 are the same instance: {db1 is db2}")
    print(f"db1 connection string: {db1.connection_string}")
    print(f"db2 connection string: {db2.connection_string}")
