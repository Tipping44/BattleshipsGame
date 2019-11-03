import User
import Ships
import Constants as c

class Grid:
    
    """Defines and holds properties of the gameboard."""

    def __init__(self):
        self.grid = [[c.Empty for row in range(c.width)] for col in range(c.height)]

    def displayGrid(self):

        colHead = ("  ABCDEFGHIJ\n")
        rowHead = [' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', '10']
        print (" ".join(colHead))
        for row in range(c.height):
            print(str(rowHead[row]), end="  ")    
            for col in range(c.width):
                currentCell = self.grid[row][col]
                if currentCell == c.liveShip:
                    print (c.Empty, end = ' ')
                else:
                    print (currentCell, end = ' ')
            print (" ")

    def isRowFree(self, row, col, size):
        gridIsEmpty = []
        for _ in range(size):
            if self.insideRowCheck(row) and self.insideColCheck(col):
                if self.grid[row][col] == c.Empty:
                    gridIsEmpty.append((row,col))
                    row += 1 
                else:
                    row += 1
            else:
                return False        
        if size == len(gridIsEmpty):
            return True
        else:
            return False    

    def isColumnFree(self, row, col, size):
        gridIsEmpty = []
        for _ in range(size):
                if self.insideColCheck(col) and self.insideRowCheck(row):
                    if self.grid[row][col] == c.Empty:
                        gridIsEmpty.append((row,col))
                        col += 1
                    else:
                        col += 1
                else:
                    return False
        if size == len(gridIsEmpty):
            return True
        else:
            return False

    def shipPlacementRow(self, row, col, size):
        for _ in range(size):
            self.grid[row][col] = c.liveShip
            row += 1
        
    def shipPlacementCol(self,row,col,size):
        for _ in range(size):
            self.grid[row][col] = c.liveShip
            col +=1
            
    def insideRowCheck(self,row):
        try:
            self.grid[row]
            return True
        except IndexError:
            return False

    def insideColCheck(self,col):
        try:
            self.grid[col]
            return True
        except IndexError:
            return False
