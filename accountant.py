
ALLOWED_COMMANDS = ('payment', 'sale', 'purchase', 'stop', 'account', 'magazine')
actions = {}  # an empty dictionary for saving all command lines: key - action_counter, value - input_list
action_counter = 0  # number of actions given by the user
account_balance = 0
account_history = {}  # key - account change, value - comment
magazine = {}  # dictionary for magazine balance: key - product, value - stock status
input_string = ''

print("Hello! Welcome to our online magazine tracker! \n "
      "You can now make some actions on your account. \n"
      f"To perform an action type as follows:\n"
      f"1. To record a payment: {ALLOWED_COMMANDS[0]} <amount in gr> <comment> \n"
      f"2. To note a sale: {ALLOWED_COMMANDS[1]} <product> <price> <number>\n"
      f"3. To note a purchase: {ALLOWED_COMMANDS[2]} <product> <price> <number>\n"
      f"4. To preview your account balance: {ALLOWED_COMMANDS[4]}\n"
      f"5. To preview your stock status: {ALLOWED_COMMANDS[5]}\n"
      f"When you are done with updates, type {ALLOWED_COMMANDS[3]} to proceed to summary.")

# actions
while input_string != 'stop':
    input_string = input("Write action: ")  # get input
    if not input_string:
        break
    input_list = input_string.split()
    command = input_list[0]
    action_counter += 1  # number of line will be the key of a dict
    actions[action_counter] = input_list  # current command line is saved
    if command in ALLOWED_COMMANDS:
        if command == 'payment':  # entering payment mode
            account_change = int(input_list[1])  # int
            comment = input_list[2]  # str
            account_balance += account_change  # update account balance
        elif command == 'account':
            print(f'Current account balance is {account_balance}.')
        elif command == 'magazine':
            print(f'Current magazine status is:\n {magazine}.')
        elif command == 'stop':
            break
        else:
            product_id = input_list[1]  # str
            price = int(input_list[2])  # int
            number = int(input_list[3])  # int
            if price > 0 and number > 0:  # price and number must be positive
                if command == 'sale':
                    if product_id in magazine:
                        if magazine[product_id] >= number:
                            magazine[product_id] -= number  # subtracting number of sold products from the magazine
                            account_balance += price * number  # adding income
                            account_history[price] = 'sale'  # adding comment to the account change
                        else:
                            print(f'Error - out of stock')
                            continue  # try again
                        if magazine[product_id] == 0:
                            del magazine[product_id]
                    else:
                        print(f'Not in offer! Pick another product')
                        continue  # try again...
                elif command == 'purchase':
                    account_balance -= price * number  # subtracting the expense
                    account_history[price] = 'purchase'  # adding the expense to account history
                    if product_id in magazine:
                        magazine[product_id] += number  # adding number of purchased products to the magazine
                        # print(f'Magazine: {product_id}: number - {magazine[product_id]}, last added - {number}')
                    else:
                        magazine[product_id] = number  # adding purchased products to the magazine
            else:
                print('Error - price and number must be positive.')
                continue  # try again
    else:
        print(f'Please write one of allowed commands: {ALLOWED_COMMANDS}')

print(f'Changes complete.')

# summary
print(f'Time to sum up. Type as follows:\n'
      f'To preview your account balance: {ALLOWED_COMMANDS[4]}.\n'
      f'or to preview stock status of chosen products: {ALLOWED_COMMANDS[5]} <product1> <product2> etc.\n'
      f'or to view account history: history')
input_string = input("Write action: ")
if input_string:  # if a user typed any action
    input_list = input_string.split()
    if input_string == 'account':
        print(f'Current account balance is {account_balance}.')
    elif input_string == 'history':
        print(f'Account history:')
        for change, comment in account_history.items():
            print(change, comment)
    elif input_list[0] == 'magazine':
        print(f'Stock status:')
        for product in input_list:
            if product in magazine:
                print(f'{product}: {magazine[product]}')
            else:
                print(f'Given product not in magazine')

# final print
print('All actions performed:')
for number, action in actions.items():
    print(number, action)
print('Good bye!')
