import pyxel

class Player:
    def __init__(self):
        self.x = 20
        self.y = 0
        self.dx = 0
        self.dy = 0

        self.dxlast = 0
        self.on_ground = False

        self.speed = 2
        self.gravity = 1.2
        self.jump_force = 8

        self.ground_level = 92

        self.sword = Sword()


    def update(self):
        self.update_x()
        self.update_y()
       

    def update_x(self):
        self.dx = 0
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.dx += self.speed
        if pyxel.btn(pyxel.KEY_LEFT):
            self.dx -= self.speed

        if self.dx == 0:
            self.dx = self.dxlast

        self.dxlast = self.dx
        self.x += self.dx


    def update_y(self):
        if self.on_ground:
            self.check_jump()
            return

        if self.is_on_ground():
            self.dy = 0
            self.y = self.ground_level
            self.on_ground = True
            self.check_jump()
            return

        self.dy = self.dy + self.gravity
        self.y += self.dy

    def is_on_ground(self):
        if self.y + self.dy >= self.ground_level:
            return True
        else:
            return False

    def check_jump(self):
        if pyxel.btn(pyxel.KEY_UP):
            self.dy = -self.jump_force
            self.on_ground = False


    def draw(self):
        pyxel.rect(self.x, self.y, 8, 8, 10)




class Sword:
    def __init__(self):
        self.x = 0
        self.y = 0

    def update(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pyxel.rect(self.x, self.y, 8, 8, 6)