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
            
class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score: 0"
        self.center = (100, 30)

class LblTime(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Time left: 10"
        self.center = (500, 30)

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("skyLine.jpg")

        self.soundMoney = simpleGE.Sound("pickupCoin.wav")
        self.numMoneys = 10
        self.score = 0
        self.lblScore = LblScore()
                   
        self.timer = simpleGE.Timer()
        self.timer.totalTime = 10
        self.lblTime = LblTime()
        
        self.chris = Chris(self)

        self.Moneys = []
        for i in range(self.numMoneys):
            self.Moneys.append(Money(self))

        self.sprites = [self.chris,
                        self.Moneys,
                        self.lblScore,
                        self.lblTime]

    def process(self):
        for money in self.Moneys:
            if money.collidesWith(self.chris):
                money.reset()
                self.soundMoney.play()
                self.score += 1
                self.lblScore.text = f"Score: {self.score}"
                
        self.lblTime.text = f"Time Left: {self.timer.getTimeLeft():.2f}"
        if self.timer.getTimeLeft() < 0:
            print(f"Score: {self.score}")
            self.stop()

def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()