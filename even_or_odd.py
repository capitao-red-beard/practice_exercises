value = int(input('Please enter a maximum value: '))

for i in range(0, value + 1):
    if i % 2 == 0:
        print(i, 'EVEN')
    else:
        print(i, 'ODD')
