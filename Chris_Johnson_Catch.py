"""Chris Johnson
Catch - Slide
5/7/24
"""

import random, pygame, simpleGE

class Money(simpleGE, Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        set.setImage("Money.png")
        self.setSize(25, 25)
        self.minSpeed = 3
        self.maxSpeed = 8


    def reset(self):
        self.y = 10

        #x is random to screen width
        self.x = random.randint(0, self.screenWidth)

        #dy is random minSpeed to maxSpeed
        self.dy = randomrandint(self.minSpeed, self.maxSpeed)

    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()

class Chris(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Chris.png")
        self.setSize(50, 50)
        self.position = (320, 400)
        self.moveSpeed = 5

    def process(self):
        if self.isKeyPresses(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPresses(pygame.K_RIGHT):
            self.x += self.moveSpeed

class Game(simpleGE, Scene):
    def __init__(self):
        super().__init__()
        self.setImage("skyline.jpg")

        self.soundMoney = simpleGE.Sound("pickupCoin.wav")
        self.chris = Chris(self)
        self.Money = Money(self)

        self.sprites = (self.chris,
                        self.money)

    def process(self):
        if self.money.collidesWith(self.chris):
            self.money.reset()
            self.soundMoney.play()




def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()