
ALLOWED_COMMANDS = ('balance', 'sale', 'purchase')

input_string = input("Command line: ") # get input
while input_string != 'end':
    # input_string = input("Command: ") # get input
    input_list = input_string.split()
    command = input_list[0]
    if command in ALLOWED_COMMANDS:
        if command == 'balance': # balance mode
            value = int(input_list[1])  # int
            comment = int(input_list[2])  # str
            print(f'Balance mode: value {value}, comment {comment}.')
        elif command == 'sale':
            product_id = input_list[1]  # str
            price = int(input_list[2])  # int
            number_sold = int(input_list[3])  # int
            print(f'Sale mode: product ID - {product_id}, price - {price}, numbers of sold items - {number_sold}.')
        elif command == 'purchase':
            product_id = input_list[1]  # str
            price = int(input_list[2])  # int
            number_sold = int(input_list[3])  # int
            print(f'Purchase mode: product ID - {product_id}, price - {price}, numbers of sold items - {number_sold}.')
    else:
        print(f'Please write one of allowed commands: {ALLOWED_COMMANDS}')
    input_string = input("Next command line: ")  # get next input

print(f'Thank you!')