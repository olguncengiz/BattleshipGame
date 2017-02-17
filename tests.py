import unittest
from board import Board
from ship import Ship
from user import User

class TestBattleship(unittest.TestCase):    
    def setUp(self):
        pass
    
    def test_board(self):
        board = Board()

        self.assertEqual(board.size, 10)
        self.assertEqual(board.chr_blank, ' ')
        self.assertEqual(board.chr_miss, 'X')
        self.assertEqual(board.chr_hit, 'O')
        
        self.assertEqual(board.isValidCellAddress('A5'), True)
        self.assertEqual(board.isValidCellAddress('Z5'), False)
        self.assertEqual(board.isValidCellAddress('A11'), False)

        self.assertEqual(board.canShootCell('A5'), True)
        board.shoot('A5')
        self.assertEqual(board.getCellValue('A5'), 'X')
        self.assertEqual(board.canShootCell('A5'), False)
        self.assertEqual(board.decode('A5'), [4, 0])
        self.assertEqual(board.encode(5, 1), 'B6')

        self.assertEqual(board.canPositionShip('J6', 0, 3), False)
        self.assertEqual(board.canPositionShip('J6', 1, 3), True)

    def test_ship(self):
        ship = Ship('Destroyer', 'D', 3, 0)

        self.assertEqual(ship.isSunk(), False)
        ship.shoot()
        self.assertEqual(ship.isSunk(), False)
        ship.shoot()
        ship.shoot()
        self.assertEqual(ship.isSunk(), True)

    def test_user(self):
        player1 = User('Olgun')

        self.assertEqual(player1.bot, False)
        self.assertEqual(player1.getShip('A').name, 'Aircraft Carrier')
        self.assertEqual(player1.getShip('B').name, 'Battleship')
        self.assertEqual(player1.getShip('A').damage, 0)
        player1.getShip('A').shoot()
        self.assertEqual(player1.getShip('A').damage, 1)
        self.assertEqual(player1.allShipsSunk(), False)
        for ship in player1.ships:
            while ship.damage < ship.length:
                ship.shoot()
        self.assertEqual(player1.allShipsSunk(), True)

        player2 = User('Bot-1', bot=True)
        self.assertEqual(player2.bot, True)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBattleship)
    unittest.TextTestRunner(verbosity=2).run(suite)