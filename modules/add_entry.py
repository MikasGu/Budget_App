from modules.entry import Entry


class AddEntry(Entry):
    def sender(self):
        return input('Enter the sender: ')

    def extra_info(self):
        return input('Enter extra info: ')
