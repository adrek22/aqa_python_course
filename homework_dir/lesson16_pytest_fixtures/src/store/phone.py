class Phone:
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def __str__(self):
        return f"{self.model} at {self.price}"
