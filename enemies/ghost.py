import pyxel
import random
import math
import modules.vector as vector


class Enemy:
    def ready(self):
        self.has_bullets = False

        starting_x = (96, 4)
        self.middle_height = 38
        self.counter = random.randint(0,99)

        self.death_animation_time = 0
        self.death_animation_frame = 0

        initial_direction = random.randint(0,1)

        self.position = vector.Vector()
        self.starting_position = vector.Vector(
                x=starting_x[initial_direction],
                y=self.get_y()
        )

        if initial_direction == 0:
            initial_direction = -1
        
        self.death_animation_frame = 0

        self.border_margin = 10
        self.speed = 0.8
        self.velocity = vector.Vector( x = initial_direction * self.speed )
        self.countdown = 32

        self.damage = 20
                

    def update(self):
        if self.countdown > 0:
            self.update_countdown()
            return

        self.counter += 1

        self.update_x()
        self.position.y = self.get_y()


    def update_countdown(self):
        self.countdown -= 1

        if self.countdown == 0:
            self.position = self.starting_position


    def update_x(self):
        if self.is_in_border():
            self.velocity.x *= -1

        self.position.x += self.velocity.x


    def get_y(self):
        return self.middle_height + math.sin(self.counter / 10) * 12


    def is_in_border(self):
        new_x = self.position.x + self.velocity.x
        if self.velocity.x > 0 and new_x < (pyxel.width - self.border_margin) or\
        self.velocity.x < 0 and new_x > (self.border_margin):
            return False

        return True


    def draw(self):
        if self.countdown > 0:
            u = (pyxel.frame_count // 2 % 2) * 8
            pyxel.blt(self.starting_position.x - 4, self.starting_position.y - 4, 0, 16 + u, 64, 8, 8, 0)
            return

        width = 8 if self.velocity.x >= 0 else -8
        u = (pyxel.frame_count // 3 % 2) * 8

        pyxel.blt(self.position.x - 4, self.position.y - 4, 0, u, 64, width, 8, 0)


    def death_animation(self):
        self.death_animation_time += 1
        width = 8 if self.velocity.x >= 0 else -8
        self.death_animation_frame = (self.death_animation_time // 3)
        u= (self.death_animation_frame) * 8

        pyxel.blt(self.position.x - 4, self.position.y - 4, 0, u, 72, width, 8, 0)

