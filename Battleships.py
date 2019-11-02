import Gameboard
import User
import Ships
import Constants

class StartGame:
    def __init__(self):
        self.playGame()

    def playGame(self):
        p = User.Player()
        p.placeShips()
        check = True 
        while check is True:
            p.fireShot()
            if p.sinkShips() is True:
                p.winMessage()
                check = False
            else:
                continue
StartGame()