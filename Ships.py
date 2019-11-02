import Constants as c

class EnemyShips():
    
    """Stores ships properties."""

    def __init__(self, shipType, size):
        self.shiptype = shipType
        self.size = size 
        self.shipLocation = []

    def dirVertical(self, row, col):
        for _ in range(self.size):
            self.shipLocation.append((row, col))
            row += 1

    def dirHorizontal(self, row, col):
        for _ in range(self.size):
            self.shipLocation.append((row, col))    
            col += 1

    def shipStatus(self):
        if self.shipLocation == []:
            return True
        else:
            return False