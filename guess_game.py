'''
simple guess game
'''

import random
def play_game():
    '''
    function for playing the play_game
    '''

    guess = random.randint(1, 10)
    chances = 3
    while chances != 0:
        usr_guess = input("Enter a number:")
        if usr_guess == guess:
            print("Congratulation!!! \nYou have won")
            break
        chances -= 1
        print("Cances remaining:", chances)
    if chances == 0:
        print("Better luck next time :(")
        print("The number was:", guess)


if __name__ == '__main__':
    play_game()
