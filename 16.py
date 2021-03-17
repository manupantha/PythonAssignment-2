class SuperMario:
    def __init__(self, name, lives, guns, height, width, killed, alive):
        self.name = name
        self.lives = lives
        self.guns = guns
        self.height = height
        self.width = width
        self.killed = killed
        self.alive = alive

    def dead(self, over):
        self.killed = over

    def life(self, lives):
        self.alive = lives
