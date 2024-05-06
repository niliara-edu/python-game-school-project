import pyxel
import random


class Enemy:
    def __init__(self):
        self.x = random.randint(10,100-8)
        self.y = 80
        self.dx = random.randint(0,1)
        if self.dx == 0: self.dx = 1
        
        self.margin = 10
        self.countdown = 0
        self.ground_level = 50

        self.speed = 0.5
        self.dx *= self.speed


    def update(self):
        if self.y > self.ground_level:
            self.y -= 0.5
            return

        if random.randint(0,20) == 20 or self.is_in_border():
            self.dx *= -1

        self.x += self.dx

 
    def is_in_border(self):
        new_x = self.x + self.dx
        if self.margin < new_x < pyxel.width - self.margin:
            return False

        return True


    def draw(self):
        w = 8 if self.dx >= 0 else -8
        u = (pyxel.frame_count // 3 % 4) * 8

        pyxel.blt(self.x - 4, self.y - 4, 0, u, 24, w, 8, 0)


    def death_anima(self):
        self.countdown += 1
        w = 8 if self.dx >= 0 else -8
        u = (self.countdown // 3 % 4) * 8

        pyxel.blt(self.x - 4, self.y - 4, 0, u, 24, w, 8, 0)


