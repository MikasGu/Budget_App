import pickle

from modules.add_entry import AddEntry
from modules.remove_entry import RemoveEntry


class Budget:
    def __init__(self):
        self.log = []

    def add_entry(self, amount):
        entry = AddEntry(amount)
        sender = entry.sender()
        extra_info = entry.extra_info()
        full_entry = [entry, sender, extra_info]
        with open("entries.pkl", 'rb') as file:
            entries = list(pickle.load(file))
            with open("entries.pkl", "wb") as file2:
                entries.append(full_entry)
                pickle.dump(entries, file2)

    def remove_entry(self, amount):
        entry = RemoveEntry(amount)
        payment_type = entry.payment_type()
        paid_for = entry.paid_for()
        full_entry = [entry, payment_type, paid_for]
        with open("entries.pkl", 'rb') as file:
            entries = list(pickle.load(file))
            with open("entries.pkl", "wb") as file2:
                entries.append(full_entry)
                pickle.dump(entries, file2)

    def get_balance(self):
        with open("entries.pkl", 'rb') as file:
            entries = list(pickle.load(file))
            sum1 = 0
            for entry in entries:
                int_i = int(str(entry[0]))
                sum1 = sum1 + int_i

            return f"Your balance is {sum1} EUR"

    def check_log(self):
        with open("entries.pkl", 'rb') as file:
            entries = list(pickle.load(file))
            print(entries)
