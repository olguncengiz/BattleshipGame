#from user import User
import common

class Game(object):
    def __init__(self, player1, player2):
        self.users = [player1, player2]

    def play(self):
        for user in self.users:
            if user.bot:
                user.positionShips()
            else:
                while True:
                    choice = raw_input('%s, Please Enter A Positioning Method (1-Auto, 2-Manual): ' % user.name)
                    if choice == '2':
                        user.positionShips(True)
                        break
                    elif choice == '1':
                        user.positionShips()
                        break
        messageBoard = ''

        turn = 0

        while True:           
            while True:
                self.printRoundMessage(self.users[turn % 2], messageBoard)

                activePlayer = self.users[turn % 2]
                otherPlayer = self.users[(turn + 1) % 2]

                cell = activePlayer.playTurn()
                if otherPlayer.primaryBoard.canShootCell(cell):
                    cellValue = otherPlayer.primaryBoard.shoot(cell)

                    if otherPlayer.primaryBoard.getCellValue(cell) == otherPlayer.primaryBoard.chr_hit:
                        activePlayer.trackingBoard.markTrackingBoard(cell, hit=True)
                        hitShip = otherPlayer.getShip(cellValue)
                        hitShip.shoot()
                        if hitShip.isSunk():
                            messageBoard = '%s Sank %s\'s %s\n' % (activePlayer.name, otherPlayer.name, hitShip.name)
                        pass
                    else:
                        activePlayer.trackingBoard.markTrackingBoard(cell, hit=False)
                        turn = turn + 1
                    break

            if otherPlayer.allShipsSunk():
                messageBoard = messageBoard + '%s Won In  %s Turns!\n' % (activePlayer.name, turn / 2)
                self.printRoundMessage(activePlayer, messageBoard)
                break

            self.printRoundMessage(activePlayer, messageBoard)
        while True:
            ok = raw_input('Type "OK" To Go To Main Menu...')
            if ok.upper() == 'OK':
                break

    def printRoundMessage(self, player, message):
        # Check if both of players are bots
        allBots = self.users[0].bot and self.users[1].bot
        if allBots or not player.bot:
            common.clearScreen()
            print 'Player: %s' % player.name
            print 'Primary Board:'
            player.primaryBoard.printBoard()
            print 'Tracking Board:'
            player.trackingBoard.printBoard()
            print 'DASHBOARD: %s' % message