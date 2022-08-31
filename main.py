from modules.budget import Budget

budget = Budget()

while True:
    procedure = input("""Choose a procedure:
    1) Add money
    2) Remove money
    3) Check balance
    4) Check log
    5) Exit
    """)
    if procedure == '1':
        budget.add_entry(int(input('Enter amount to add: ')))
    if procedure == '2':
        budget.remove_entry(-int(input('Enter amount to remove: ')))
    if procedure == '3':
        print(budget.get_balance())
    if procedure == '4':
        print(budget.check_log())
    if procedure == '5':
        print('Thank you, bye!')
        break
