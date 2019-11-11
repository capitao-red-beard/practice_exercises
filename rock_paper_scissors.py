guess = 'please make a rock, paper or scissors guess: '
play = True

def play_again():
    answer = input('Would you like to play again? ')
    if answer != 'y':
        play = False

while play:
    p1 = input(f'Player {1} {guess}')
    p2 = input(f'Player {2} {guess}')

    if p1 == p2:
        print("It's a tie")
    elif p1 == 'rock' and p2 == 'scissors':
        print('p1 wins')
        play = play_again()
    elif p1 == 'scissors' and p2 == 'paper':
        print('p1 wins')
        play = play_again()
    elif p1 == 'paper' and p2 == 'rock':
        print('p1 wins')
        play = play_again()
    else:
        print('p2 wins')
        play = play_again()
