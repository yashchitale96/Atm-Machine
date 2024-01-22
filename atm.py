import getpass

users = ['yash', 'sonal', 'ram']
pins = ['2003', '1234', '4321']
amounts = [10000, 15000, 30000]
transaction_history = {user: [] for user in users}
MAX_PIN_ATTEMPTS = 3

def get_user():
    while True:
        user = input('\nENTER USER NAME: ').lower()
        if user in users:
            return users.index(user)
        else:
            print('----------------')
            print('****************')
            print('INVALID USERNAME')
            print('****************')
            print('----------------')

def check_pin(user_index):
    count = 0
    while count < MAX_PIN_ATTEMPTS:
        pin = getpass.getpass('PLEASE ENTER PIN: ')
        if pin.isdigit():
            if pin == pins[user_index]:
                return True
            else:
                count += 1
                print('-----------')
                print('***********')
                print('INVALID PIN')
                print('***********')
                print('-----------')
                print()
        else:
            print('------------------------')
            print('************************')
            print('PIN CONSISTS OF 4 DIGITS')
            print('************************')
            print('------------------------')
            count += 1
    return False

def main_menu(user_index):
    while True:
        print('-------------------------------')
        print('*******************************')
        response = input('SELECT FROM FOLLOWING OPTIONS: \nStatement__(S) \nWithdraw___(W) \nLodgement__(L)  \nChange PIN_(P)  \nTransfer__(T) \nHistory____(H) \nQuit_______(Q) \n: ').lower()
        print('*******************************')
        print('-------------------------------')
        
        if response == 's':
            print_statement(user_index)
        elif response == 'w':
            withdraw(user_index)
        elif response == 'l':
            lodge(user_index)
        elif response == 'p':
            change_pin(user_index)
        elif response == 't':
            transfer_money(user_index)
        elif response == 'h':
            show_transaction_history(user_index)
        elif response == 'q':
            print('Goodbye!')
            break
        else:
            print('------------------')
            print('******************')
            print('RESPONSE NOT VALID')
            print('******************')
            print('------------------')

def print_statement(user_index):
    print('---------------------------------------------')
    print('*********************************************')
    print(users[user_index], 'YOU HAVE ', amounts[user_index],'EURO ON YOUR ACCOUNT.')
    print('*********************************************')
    print('---------------------------------------------')
    
def withdraw(user_index):
    print('---------------------------------------------')
    print('*********************************************')
    cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
    print('*********************************************')
    print('---------------------------------------------')
    if cash_out % 10 != 0:
        print('------------------------------------------------------')
        print('******************************************************')
        print('AMOUNT YOU WANT TO WITHDRAW MUST TO MATCH 10 EURO NOTES')
        print('******************************************************')
        print('------------------------------------------------------')
    elif cash_out > amounts[user_index]:
        print('-----------------------------')
        print('*****************************')
        print('YOU HAVE INSUFFICIENT BALANCE')
        print('*****************************')
        print('-----------------------------')
    else:
        amounts[user_index] -= cash_out
        transaction_history[users[user_index]].append(f'Withdraw: {cash_out} EURO')
        print('-----------------------------------')
        print('***********************************')
        print('YOUR NEW BALANCE IS: ', amounts[user_index], 'EURO')
        print('***********************************')
        print('-----------------------------------')

def lodge(user_index):
    print()
    print('---------------------------------------------')
    print('*********************************************')
    cash_in = int(input('ENTER AMOUNT YOU WANT TO LODGE: '))
    print('*********************************************')
    print('---------------------------------------------')
    print()
    if cash_in % 10 != 0:
        print('----------------------------------------------------')
        print('****************************************************')
        print('AMOUNT YOU WANT TO LODGE MUST TO MATCH 10 EURO NOTES')
        print('****************************************************')
        print('----------------------------------------------------')
    else:
        amounts[user_index] += cash_in
        transaction_history[users[user_index]].append(f'Lodge: {cash_in} EURO')
        print('----------------------------------------')
        print('****************************************')
        print('YOUR NEW BALANCE IS: ', amounts[user_index], 'EURO')
        print('****************************************')
        print('----------------------------------------')

def change_pin(user_index):
    print('-----------------------------')
    print('*****************************')
    new_pin = getpass.getpass('ENTER A NEW PIN: ')
    print('*****************************')
    print('-----------------------------')
    if new_pin.isdigit() and new_pin != pins[user_index] and len(new_pin) == 4:
        print('------------------')
        print('******************')
        new_ppin = getpass.getpass('CONFIRM NEW PIN: ')
        print('*******************')
        print('-------------------')
        if new_ppin != new_pin:
            print('------------')
            print('************')
            print('PIN MISMATCH')
            print('************')
            print('------------')
        else:
            pins[user_index] = new_pin
            print('NEW PIN SAVED')
    else:
        print('-------------------------------------')
        print('*************************************')
        print('   NEW PIN MUST CONSIST OF 4 DIGITS \nAND MUST BE DIFFERENT TO PREVIOUS PIN')
        print('*************************************')
        print('-------------------------------------')

def transfer_money(sender_index):
    print('----------------------------------')
    print('**********************************')
    receiver = input('Enter the username to transfer money to: ')
    print('**********************************')
    print('----------------------------------')

    if receiver in users and receiver != users[sender_index]:
        amount = int(input('Enter the amount to transfer: '))
        if amount > 0 and amount <= amounts[sender_index]:
            amounts[sender_index] -= amount
            amounts[users.index(receiver)] += amount
            transaction_history[users[sender_index]].append(f'Transfer to {receiver}: {amount} EURO')
            transaction_history[receiver].append(f'Transfer from {users[sender_index]}: {amount} EURO')
            print('----------------------------------')
            print('**********************************')
            print(f'{amount} EURO transferred to {receiver}')
            print('**********************************')
            print('----------------------------------')
        else:
            print('----------------------------')
            print('****************************')
            print('Invalid amount or insufficient balance for the transfer.')
            print('****************************')
            print('----------------------------')
    else:
        print('----------------------------')
        print('****************************')
        print('Invalid username for transfer.')
        print('****************************')
        print('----------------------------')

def show_transaction_history(user_index):
    print('-----------------------------------')
    print('***********************************')
    print(f'Transaction History for {users[user_index]}:')
    for transaction in transaction_history[users[user_index]]:
        print(transaction)
    print('***********************************')
    print('-----------------------------------')

# Main part of the program
user_index = get_user()
if not check_pin(user_index):
    print('-----------------------------------')
    print('***********************************')
    print('Too many unsuccessful attempts. Exiting...')
    print('***********************************')
    print('-----------------------------------')
else:
    print('-------------------------')
    print('*************************')
    print('LOGIN SUCCESSFUL, CONTINUE')
    print('*************************')
    print('-------------------------')
    print()
    print('--------------------------')
    print('**************************')   
    print(str.capitalize(users[user_index]), 'welcome to ATM')
    print('**************************')
    print('----------ATM SYSTEM-----------')
    main_menu(user_index)
