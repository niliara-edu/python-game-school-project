import pyxel
import random
import modules.vector as vector


class Enemy:
    def __init__(self):
        starting_x = random.randint(10,90)
        bottom_y_position = 0

        self.position = vector.Vector(
                x=starting_x,
                y=bottom_y_position
        )

        initial_direction = random.randint(0,1)
        if initial_direction == 0:
            initial_direction = -1
        
        self.respawn_time = 0
        self.death_animation_frame = 0

        self.border_margin = 10
        self.height_level = 35
        self.chance_to_flip = 50

        self.descend_speed = 0.75
        self.speed = 0.7
        self.velocity = vector.Vector( x = initial_direction * self.speed )


    def update(self):
        if self.position.y < self.height_level:
            self.position.y += self.descend_speed
            return

        if random.randint(0,self.chance_to_flip) == 0 or self.is_in_border():
            self.velocity.x *= -1

        self.position.x += self.velocity.x

 
    def is_in_border(self):
        new_x = self.position.x + self.velocity.x
        if self.border_margin < new_x < (pyxel.width - self.border_margin):
            return False

        return True


    def draw(self):
        width = 8 if self.velocity.x >= 0 else -8
        u = (pyxel.frame_count // 3 % 4) * 8

        pyxel.blt(self.position.x - 4, self.position.y - 4, 0, u, 32, width, 8, 0)


    def death_animation(self):
        self.death_animation_frame += 1
        width = 8 if self.velocity.x >= 0 else -8
        u= (self.death_animation_frame // 3 % 4) * 8

        pyxel.blt(self.position.x - 4, self.position.y - 4, 0, u, 56, width, 8, 0)

