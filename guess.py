number = int(input('Please enter a number between 0 and 100 for the computer to guess: '))
low = 0
high = 100
total_guesses = 0
guess = 50

while True:
    total_guesses += 1
    print(f'The computer guessed {guess}')

    if guess == number:
        print(f'The computer guessed your number, it took {total_guesses} guesses.')
        break

    elif guess < number:
        low = guess + 1
        guess = low + round((high - low) / 2)

    elif guess > number:
        high = guess - 1
        guess = high - round((high - low) / 2)
