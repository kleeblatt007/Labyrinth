class Position(object):
    """Position mit x und y Wert"""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def setPosition(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return int(self.x)

    def getY(self):
        return int(self.y)

    def __gt__(self, other):
        return self.x == other.getX and self.y == other.getY