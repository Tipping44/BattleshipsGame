import Gameboard
import Ships
import random
import Constants as c 

class Player:

    
    """Holds properties of the player.""" 
    
    shipList = {"Battleship": 5, "Destroyer1": 4, "Destroyer2": 4}

    def __init__(self):
        self.grid = Gameboard.Grid()
        self.enemySquad = []

    def placeShips(self):
        shipPositions = ["V", "H"]

        for ship, size in self.shipList.items():
            place = True 
            while place:
                row = random.randint(0,9)
                col = random.randint(0,9)
                randomAxis = random.choice(shipPositions)

                if randomAxis == "V":
                    if self.grid.isRowFree(row, col, size):
                        self.grid.shipPlacementRow(row, col, size)
                        aShip = Ships.EnemyShips(ship, size)
                        aShip.dirVertical(row, col)
                        self.enemySquad.append(aShip)
                        place = False
                    else:
                        row += 2
                elif randomAxis == "H":
                    if self.grid.isColumnFree(row, col, size):
                        self.grid.shipPlacementCol(row, col, size) 
                        aShip = Ships.EnemyShips(ship, size)
                        aShip.dirHorizontal(row, col)
                        self.enemySquad.append(aShip)
                        place = False
                    else: 
                        col += 2
                else:
                    continue                            
                    
    def fireShot(self):
        dictionaryList = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9}

        self.viewGrid()
        while True:
            try:
                userInput = input("\nEnter your shot coordinates: ").upper()
                if not userInput:
                    raise ValueError
                else:
                    pass
                column = userInput[0]
                col = dictionaryList.get(column, "")
                row = int(userInput[1:])
                row -=1 
                assert -1 < row <10
            except ValueError:
                print("\nPlease enter valid coordinates!!")
            except AssertionError:
                print("\nPlease pick a number between 1 and 10")
            else:
                break
        try: 
            if self.grid.insideRowCheck(row) and self.grid.insideColCheck(col):
                if self.grid.grid[row][col] == c.liveShip: 
                    print("\nDirect Hit!!\n")
                    self.grid.grid[row][col] = c.Hit
                    self.isHit(row,col)
                else:
                    if self.grid.grid[row][col] == c.Miss:
                        print ("\nAlready fired there!\n")
                        self.fireShot()
                    elif self.grid.grid[row][col] == c.Hit:
                        print ("\nAlready fired there!\n")
                        self.fireShot()
                    else:
                        print ("\nShot MISS!\n")
                        self.grid.grid[row][col] = c.Miss

        except TypeError:
            print ("\nYou need to enter a valid position\n")

        except ValueError:
            print ("\nYou need to enter a valid position\n")
            self.fireShot()

    def viewGrid(self):
        self.grid.displayGrid()

    def isHit(self, row, col):
        for aShip in self.enemySquad:
            if (row, col) in aShip.shipLocation:
                aShip.shipLocation.remove((row, col))
                if aShip.shipStatus():
                    self.enemySquad.remove(aShip)
                    print("\nYou have sunk a ship!!\n")            

    def sinkShips(self):
        shipCount = 0
        for row in range(len(self.grid.grid)):
            for col in range(len(self.grid.grid)):
                if self.grid.grid[row][col] == c.liveShip:
                    shipCount += 1 
        if shipCount == 0:
            return True
        else:
            return False

    def winMessage(self):
        print("\nCongratulations, you have sunk all of the enemy ships!\n")
