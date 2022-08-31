import pickle

from modules.budget import Budget

# with open("entries.pkl", 'wb') as file:
#     empt = ''
#     pickle.dump(empt, file)
budget = Budget()

while True:
    procedure = input("""Choose a procedure:
    1) Add money
    2) Remove money
    3) Check balance
    4) Check log
    5) Clear log
    6) Exit
    """)
    if procedure == '1':
        budget.add_entry(int(input('Enter amount to add: ')))
    if procedure == '2':
        budget.remove_entry(-int(input('Enter amount to remove: ')))
    if procedure == '3':
        print(budget.get_balance())
    if procedure == '4':
        budget.check_log()
    if procedure == '5':
        with open("entries.pkl", "wb") as file:
            clear = ''
            pickle.dump('', file)
    if procedure == '6':
        print('Thank you, bye!')
        break
