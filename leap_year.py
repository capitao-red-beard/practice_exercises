year = int(input('Please enter a year: '))

if year % 4 != 0:
    print(f'The year {year} is not a leap year.')
elif year % 100 != 0:
    print(f'The year {year} is a leap year.')
elif year % 400 != 0:
    print(f'The year {year} is not a leap year.')
else:
    print(f'The year {year} is a leap year.')
