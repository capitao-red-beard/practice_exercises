value = int(input("Please choose a number to divide: "))

for n in range(1, value + 1):
    if value % n == 0:
        print(n)
