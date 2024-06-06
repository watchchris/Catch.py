import pygame
import simpleGE
import random

class Money(simpleGE.Sprite):
    def __init__(self, Scene):
        super().__init__(Scene)
        self.setImage("Money.png")
        self.setSize(25, 25)
        self.minSpeed = 3
        self.maxSpeed = 8
        self.reset()

    def reset(self):
        self.y = 10
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint(self.minSpeed, self.maxSpeed)

    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()

class Chris(simpleGE.Sprite):
    def __init__(self, Scene):
        super().__init__(Scene)
        self.setImage("Chris.png")
        self.setSize(100, 100)
        self.position = (320, 400)
        self.moveSpeed = 5

    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("skyLine.jpg")

        self.soundMoney = simpleGE.Sound("pickupCoin.wav")
        self.numMoneys = 10
        self.chris = Chris(self)

        self.Moneys = []
        for i in range(self.numMoneys):
            self.Moneys.append(Money(self))

        self.sprites = [self.chris,
                        self.Moneys]

    def process(self):
        for money in self.Moneys:
            if money.collidesWith(self.chris):
                money.reset()
                self.soundMoney.play()

def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()