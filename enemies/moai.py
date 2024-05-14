import pyxel
import random
import modules.vector as vector


class Enemy:
    def __init__(self):
        starting_x = random.randint(10,90)
        top_y_position = -8

        self.position = vector.Vector(
                x=starting_x,
                y=top_y_position
        )

        self.death_animation_time = 0
        self.death_animation_frame = 0

        self.ground_level = 50
        self.speed = 1
        self.velocity = vector.Vector( y = self.speed )


    def update(self):
        if self.position.y < self.ground_level:
            self.position.y += self.velocity.y
            return

    def draw(self):
        pyxel.blt(self.position.x - 4, self.position.y - 4, 0, 0, 40, 8, 8, 0)


    def death_animation(self):
        self.death_animation_time += 1
        width = 8 if self.velocity.x >= 0 else -8
        self.death_animation_frame = (self.death_animation_time // 3)
        u = self.death_animation_frame * 8

        pyxel.blt(self.position.x - 4, self.position.y - 4, 0, u, 48, width, 8, 0)

