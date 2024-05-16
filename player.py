import pyxel
import modules.vector as vector

class Player:
    def ready(self):
        starting_x = pyxel.width / 2
        self.position = vector.Vector( x=starting_x )
        self.velocity = vector.Vector()
        self.hp = 100

        self.is_hurt = False
        self.was_on_ground = False

        self.speed = 1
        self.gravity = 0.8
        self.jump_force = 6
        self.border_margin = 10
        self.ground_level = 50

        self.sword = Sword()


    def update(self):
        self.update_x()
        self.update_y()
        self.sword.update( self.position, self.velocity.x )
        xpos = self.position.x
       

    def update_x(self):
        new_x_velocity = 0
        if pyxel.btn(pyxel.KEY_RIGHT):
            new_x_velocity += self.speed
        if pyxel.btn(pyxel.KEY_LEFT):
            new_x_velocity -= self.speed

        if new_x_velocity != 0:
            self.velocity.x = new_x_velocity

        if self.is_in_border():
            return

        self.position.x += self.velocity.x


    def update_y(self):
        if self.was_on_ground:
            self.check_jump()
            return

        if self.is_on_ground():
            self.velocity.y = 0
            self.position.y = self.ground_level
            self.was_on_ground = True
            self.check_jump()
            return

        self.velocity.y = self.velocity.y + self.gravity
        self.position.y += self.velocity.y

    def is_on_ground(self):
        if self.position.y + self.velocity.y >= self.ground_level:
            return True
        else:
            return False

    def is_in_border(self):
        new_x = self.position.x + self.velocity.x
        if self.border_margin < new_x < (pyxel.width - self.border_margin):
            return False

        return True

    def check_jump(self):
        if pyxel.btn(pyxel.KEY_UP):
            self.velocity.y = -self.jump_force
            self.was_on_ground = False

            
    def hurt(self, damage):
        self.hp -= damage
        self.is_hurt = True


    def heal(self):
        self.hp += 20
        if self.hp > 100:
            self.hp = 100


    def draw(self):
        width = 8 if self.velocity.x >= 0 else -8
        if not self.was_on_ground:
            if self.velocity.y < 0:
                frame = 16
            elif self.velocity.y > 0:
                frame = 24

        elif self.velocity.x == 0:
            frame = 0
        else:
            frame = (pyxel.frame_count // 3 % 4) * 8

        if self.is_hurt:
            v = 8
        else:
            v = 0

        pyxel.blt(self.position.x - 4, self.position.y - 4, 0, frame, v, width, 8, 0)
        self.sword.draw(-1 if frame>0 else 0)




class Sword:
    def __init__(self):
        self.position = vector.Vector()
        self.direction = 1
        self.length = 6
        self.distance_to_player = 4

    def update(self, player_position, player_velocity_x):
        if player_velocity_x == 0:
            self.direction = 1
        else:
            self.direction = player_velocity_x / abs(player_velocity_x)

        self.position.x = player_position.x + self.distance_to_player * self.direction
        self.position.y = player_position.y

    def draw(self, extra_y = 0):
        w = self.direction * 8
        pyxel.blt(self.position.x - 4, self.position.y - 4 + extra_y, 0, 0, 16, w, 8, 0)
