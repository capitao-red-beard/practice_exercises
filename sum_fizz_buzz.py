value = int(input('Please input a max value: '))

def sum_values(maximum):
    total = 0
    for i in range(0, maximum + 1):
        if i % 3 == 0:
            total += i
        elif i % 5 == 0:
            total += i
    return total

print(sum_values(value))