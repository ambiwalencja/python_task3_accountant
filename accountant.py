
ALLOWED_COMMANDS = ('balance', 'sale', 'purchase', 'stop')
actions = {}  # an empty dictionary for saving all command lines: key - action_counter, value - input_list
action_counter = 0  # number of actions given by the user
account_balance = 0
account_history = {}  # key - account change, value - comment
magazine = {}  # dictionary for magazine balance: key - product, value - stock status
input_string = ''

# actions
while input_string != 'stop':
    input_string = input("Action: ")  # get input
    input_list = input_string.split()
    command = input_list[0]
    action_counter += 1  # number of line will be the key of a dict
    actions[action_counter] = input_list  # current command line is saved
    if command in ALLOWED_COMMANDS:
        if command == 'balance':  # balance mode
            account_change = int(input_list[1])  # int
            comment = input_list[2]  # str
            account_balance += account_change  # update account balance
            # print(f'Balance mode: change on the account: {account_change}, comment: {comment}.')
        elif command == 'stop':
            break
        else:
            product_id = input_list[1]  # str
            price = int(input_list[2])  # int
            number = int(input_list[3])  # int
            if price > 0 and number > 0:  # price and number must be positive
                if command == 'sale':
                    if product_id in magazine:
                        if magazine[product_id] > number:
                            magazine[product_id] -= number  # subtracting number of sold products from the magazine
                            account_balance += price * number  # adding income
                            account_history[price] = 'sale'  # adding comment to the account change
                        else:
                            print(f'Error - out of stock')
                            continue  # try again
                    else:
                        print(f'Not in offer! Pick another product')
                        continue  # try again...
                elif command == 'purchase':
                    account_balance -= price * number  # subtracting the expense
                    account_history[price] = 'purchase'  # adding the expense to account history
                    if product_id in magazine:
                        magazine[product_id] += number  # adding number of purchased products to the magazine
                        print(f'HELP: Magazine: {product_id}: number - {magazine[product_id]}, last added - {number}')
                    else:
                        magazine[product_id] = number  # adding purchased products to the magazine
                    # print(f'Purchase mode: product ID - {product_id}, '
                    #      f' price - {price}, numbers of sold items - {number}.')
            else:
                print('Error - price and number must be positive.')
                continue  # try again
    else:
        print(f'Please write one of allowed commands: {ALLOWED_COMMANDS}')
    # input_string = input("Next action: ")  # get next input

print(f'Changes complete.')

# prints with stock/account status
input_string = input("Write next action:")
if input_string == 'account':
    print(f'Current account balance is {account_balance}.')
elif input_string == 'account history':
    print(f'Account history:')
    for change, comment in account_history.items():
        print(change, comment)
    print('Good bye!')
elif input_string.split()[0] == 'magazine':
    print(f'Stock status: {magazine}.')

# final print
print('All actions performed:')
for number, action in actions.items():
    print(number, action)
print('Good bye!')
