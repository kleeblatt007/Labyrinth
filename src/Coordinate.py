class Coordinate(object):
    '''
    speichert X- und Y-Wert
    '''
    def __init__(self, x, y, z = 0, w = 0):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def X(self):
        '''
        gibt X-Wert zurück
        :return: int
        '''
        return self.x

    def Y(self):
        '''
        gibt Y-Wert zurück
        :return: int
        '''
        return self.y

    def Z(self):
        return self.z

    def W(self):
        return self.x

    def setCoordinates(self, x, y, z = 0, w = 0):
        self.x = x
        self.y = y
        self.z = z
        self.w = w