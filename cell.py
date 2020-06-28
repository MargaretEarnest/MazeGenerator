class Cell:
    def __init__(self, wallList):
        # list of 4 walls or None where there is no wall, in order of top, right, bottom, left
        self.walls = wallList

    def getWalls(self):
        return self.walls
