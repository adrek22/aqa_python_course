class Catalog:
    def __init__(self):
        self._phones = []

    @property
    def phones(self):
        return self._phones

    @phones.deleter
    def phones(self):
        self._phones.clear()

    def add_phone(self, phone):
        self.phones.append(phone)
        print(f"Phone {phone.model} added to catalog.")

    def remove_phone(self, model):
        obj = [phone for phone in self.phones if phone.model == model][0]
        if obj:
            return self.phones.pop(self.phones.index(obj))
        return None

