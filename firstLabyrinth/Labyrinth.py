import random

class Position(object):
    """Position mit x und y Wert"""

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def setPosition(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def __gt__(self, other):
        return self.__x == other.getX() and self.__y == other.getY()


class Labyrinth(object):
    """Ein Labyrinth als 2D array, bekommt ein int size"""

    def __init__(self, start=Position(0, 0), end=Position(0, 0), size=0):
        self.__size = size
        self.__lab = [[0 for i in range(size)] for x in range(size)]
        self.__start = start
        self.__end = end

    def possiblePosition(self):
        """gibt alle Positionen die 0 sind zurück"""
        positons = []
        for x in range(self.__size):
            for y in range(self.__size):
                if self.__lab[x][y] == 0:
                    positons.append(Position(x, y))
        return positons

    def __str__(self):
        s = ""
        for x in range(self.__size):
            for y in range(self.__size):
                s += str(self.__lab[x][y]) + " "
            s += "\n"
        return s

    def getLab(self):
        return self.__lab

    def path(self):
        """erstellt ein random Pfad"""
        pos = Position(self.__start.getX(), self.__start.getY())

        while not pos.__gt__(self.__end):
            # x legt fest, ob nächster Schritt nach links, rechts oder unten geht
            x = random.randint(0, 3)
            # naechster Schritt nach links
            if x == 0 and pos.getY() - 1 >= 0:
                pos.setY(pos.getY() - 1)
                self.__lab[pos.getX()][pos.getY()] = 0
            # naechster Schritt nach rechts
            elif x == 1 and pos.getY() + 1 < self.__size:
                pos.setY(pos.getY() + 1)
                self.__lab[pos.getX()][pos.getY()] = 0
            # elif x == 2 and pos.getX() -1 >= 0:
            #    pos.setX(pos.getX()-1)
            #   self.__lab[pos.getX()][pos.getY()] = 0

            # naechster Schritt nach unten
            elif x == 3 and pos.getX() + 1 < self.__size:
                pos.setX(pos.getX() + 1)
                self.__lab[pos.getX()][pos.getY()] = 0

    def randomLab(self):
        """geht das 2D array durch und setzt random 1 oder 0 und erstellt einen Pfad"""

        # random 1 oder 0
        for p in self.possiblePosition():
            self.__lab[p.getX()][p.getY()] = random.randint(0, 1)

        # Pfad wird erstellt
        self.path()

        # Wand am Rand setzen
        for x in range(self.__size):
            self.__lab[x][0] = 1
            self.__lab[x][self.__size - 1] = 1
            self.__lab[0][x] = 1
            self.__lab[self.__size - 1][x] = 1

        # Start und Ende auf 0 setzten
        self.__lab[self.__start.getX()][self.__start.getY()] = 0
        self.__lab[self.__end.getX()][self.__end.getY()] = 0


if __name__ == '__main__':
    start = Position(0, 1)
    end = Position(4, 3)
    lab = Labyrinth(start, end, 5)
    print(lab)
    lab.randomLab()
    print(lab)
