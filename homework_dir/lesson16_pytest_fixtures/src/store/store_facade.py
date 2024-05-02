from .catalog import Catalog
from .phone import Phone


class StoreFacade:
    def __init__(self):
        self.catalog = Catalog()

    def add_phone_to_catalog(self, model, price):
        phone = Phone(model, price)
        self.catalog.add_phone(phone)
        return phone

    def remove_phone_from_catalog(self, model):
        return self.catalog.remove_phone(model)

    def show_catalog(self):
        return self.catalog.phones
