from game import Game
from user import User
import common

def printMenu():
    common.clearScreen()
    print 'Menu'
    print '1-New Game'
    print '2-Exit'

# Main Application Flow:
if __name__ == '__main__':    
    while True:
        printMenu()
        choice = raw_input()
        if choice == '2':
            common.clearScreen()
            break
        elif choice == '1':
            common.clearScreen()

            name1 = raw_input('Please Enter A Name For Player-1: ')
            bot1 = raw_input('Please Select Player Type For %s (1-Bot, 2-Real User): ' % name1)
            easy = True
            bot = False
            if bot1 == '1':
                bot = True
                difficulty = raw_input('Please Select Player Difficulty For %s (1-Easy, 2-Hard): ' % name1)
                if difficulty == '2':
                    easy = False
            player1 = User(name1, bot, easy)

            name2 = raw_input('Please Enter A Name For Player-2: ')
            bot2 = raw_input('Please Select Player Type For %s (1-Bot, 2-Real User): ' % name2)
            easy = True
            bot = False
            if bot2 == '1':
                bot = True
                difficulty = raw_input('Please Select Player Difficulty For %s (1-Easy, 2-Hard): ' % name2)
                if difficulty == '2':
                    easy = False
            player2 = User(name2, bot, easy)
            
            g = Game(player1, player2)
            g.play()
