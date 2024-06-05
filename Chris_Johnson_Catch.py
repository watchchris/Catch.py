"""Chris Johnson
Catch - Slide
5/7/24
"""

import random, pygame, simpleGE

class Chris(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Chris.png")
        self.setsize(50, 50)
        self.position = (320, 400)

class Game(simpleGE, Scene):
    def __init__(self):
        super().__init__()
        self.setImage("skyline.jpg")
        self.chris = Chris(self)
        self.sprites = (self.chris)


def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()