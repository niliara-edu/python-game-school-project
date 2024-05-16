import pyxel
import random
import modules.vector as vector
import player


class Enemy:
    def ready(self):
        self.has_bullets = False

        self.position = vector.Vector()
        self.fall()

        self.death_animation_time = 0
        self.death_animation_frame = 0

        self.ground_level = 50
        self.speed = 2
        self.velocity = vector.Vector( y = self.speed )

        self.countdown = 96

        self.damage = 30


    def update(self):
        if self.position.y < self.ground_level:
            self.position.y += self.velocity.y
            return

        self.countdown -= 1
        self.damage = 10

        if self.countdown < -(3*5):
            self.fall()
            self.countdown = 96
            return


    def fall(self):
        self.damage = 30
        top_y_position = -8
        self.position.x = random.randint(20,80)
        self.position.y = top_y_position


    def draw(self):

        if self.countdown <= 0:
            u = abs(self.countdown // 3) * 8
            pyxel.blt(self.position.x - 4, self.position.y - 4, 0, u, 40, 8, 8, 0)
        else:
            pyxel.blt(self.position.x - 4, self.position.y - 4, 0, 8, 16, 8, 8, 0)


    def death_animation(self):
        self.death_animation_time += 1
        width = 8 if self.velocity.x >= 0 else -8
        self.death_animation_frame = (self.death_animation_time // 3)
        u = self.death_animation_frame * 8

        pyxel.blt(self.position.x - 4, self.position.y - 4, 0, u, 40, width, 8, 0)

