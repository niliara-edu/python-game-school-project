import pyxel
import random
import modules.vector as vector


class Enemy:
    def ready(self):
        self.has_bullets = True
        self.bullets = []
        
        starting_x = (90, 10)
        top_y_position = -10

        initial_direction = random.randint(0,1)

        self.position = vector.Vector(
                x=starting_x[initial_direction],
                y=top_y_position
        )

        self.velocity = vector.Vector()

        if initial_direction == 0:
            self.direction = -1
        else:
            self.direction = 1
        
        self.death_animation_time = 0
        self.death_animation_frame = 0

        self.ground_level = 50
        self.falling_speed = 2
        self.speed = 0.7
        self.jump_force = 4
        self.gravity = 1
        self.delay = 80
        self.countdown = self.delay / 2
        self.initial_falling = True

        self.damage = 20


    def update(self):
        if self.initial_falling:
            if self.position.y < self.ground_level:
                self.position.y += self.falling_speed
                return

            self.initial_falling = False

        self.countdown -= 1
        if self.countdown <= 0:
            self.update_shot()


    def update_shot(self):
        self.position.y += self.velocity.y
        self.velocity.y += self.gravity

        if self.position.y >= self.ground_level:
            if self.countdown == 0:
                self.jump()
                return

            self.shoot()
            self.countdown = self.delay
            self.velocity.y = 0


    def jump(self):
        self.velocity.y = -self.jump_force


    def shoot(self):
        banana_instance = Banana()
        banana_instance.ready(self.position, self.direction)
        self.bullets.append(banana_instance)


    def draw(self):
        width = 8 * self.direction
        u = (pyxel.frame_count // 4 % 2) * 8

        pyxel.blt(self.position.x - 4, self.position.y - 4, 0, u, 88, width, 8, 0)

        for bullet in self.bullets:
            bullet.draw()


    def death_animation(self):
        self.death_animation_time += 1
        width = 8 * self.direction
        self.death_animation_frame = self.death_animation_time // 3
        u = self.death_animation_frame * 8

        pyxel.blt(self.position.x - 4, self.position.y - 4, 0, u, 56, width, 8, 0)




class Banana():
    def ready(self, position, direction):
        self.position = vector.Vector()
        self.position.x = position.x
        self.position.y = position.y - 1
        self.direction = direction
        self.speed = 1 * direction

        self.damage = 10

    def update(self):
        self.position.x += self.speed

    def draw(self):
        width = 8 * self.direction
        u = (pyxel.frame_count // 3 % 4) * 8

        pyxel.blt(self.position.x - 4, self.position.y - 4, 0, u, 80, width, 8, 0)


