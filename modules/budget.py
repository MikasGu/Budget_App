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
        self.log.append([entry, sender, extra_info])

    def remove_entry(self, amount):
        entry = RemoveEntry(amount)
        payment_type = entry.payment_type()
        paid_for = entry.paid_for()
        self.log.append([entry, payment_type, paid_for])

    def get_balance(self):
        sum1 = 0
        for i in self.log:
            int_i = int(str(i[0]))
            sum1 = sum1 + int_i

        return f"Your balance is {sum1} EUR"

    def check_log(self):
        return f"Your entries: {self.log}"
