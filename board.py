vertical = '|   '
horizontal = ' --- '

board_size = int(input('Please enter how big your grid should be: '))

for i in range(board_size):
    print(horizontal * board_size)
    print(vertical * (board_size + 1))
