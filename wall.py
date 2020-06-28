class Wall:

    def __init__(self):
        self.exists = True
        self.owner = []

    def breakWall(self):
        self.exists = False

    def addOwner(self, newOwner):
        self.owner.append(newOwner)
