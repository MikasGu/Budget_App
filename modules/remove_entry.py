from modules.entry import Entry


class RemoveEntry(Entry):
    def payment_type(self):
        return input('Enter payment type: ')

    def paid_for(self):
        return input('What did you pay for?: ')
