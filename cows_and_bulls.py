from random import randint

random_value = randint(1000, 9999)
total_guesses = 0

while True:
    cows = 0
    bulls = 0
    guess = input('Please make a guess at the 4-digit number: ')
    if guess == 'exit':
        break

    total_guesses += 1

    if int(guess) == random_value:
        print(f'You guessed the correct number, it was {random_value}, it took you {total_guesses} guesses.')
        break

    for i, g in enumerate(list(guess), 0):
        if g == list(str(random_value))[i]:
            cows += 1
        if g in list(str(random_value)):
            bulls += 1

    print(f'cows: {cows}, bulls: {bulls}')
