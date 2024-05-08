import pyxel

class Player:
    def __init__(self):
        self.x = pyxel.width / 2
        self.y = 0
        self.dx = 0
        self.dy = 0

        self.dxlast = 0
        self.on_ground = False

        self.speed = 1
        self.gravity = 0.8
        self.jump_force = 6
        self.margin = 10

        self.ground_level = 50

        self.sword = Sword()


    def update(self):
        self.update_x()
        self.update_y()
        self.sword.update( self.x, self.y, self.dxlast )
       

    def update_x(self):
        self.dx = 0
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.dx += self.speed
        if pyxel.btn(pyxel.KEY_LEFT):
            self.dx -= self.speed

        if self.is_in_border():
            self.dx = 0
            return

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

    def is_in_border(self):
        new_x = self.x + self.dx
        if self.margin < new_x < pyxel.width - self.margin:
            return False

        return True

    def check_jump(self):
        if pyxel.btn(pyxel.KEY_UP):
            self.dy = -self.jump_force
            self.on_ground = False


    def draw(self):
        w = 8 if self.dxlast >= 0 else -8 # From pyxel plattformer example

        if not self.on_ground:
            if self.dy < 0:
                u = 16
            if self.dy > 0:
                u = 24

        elif self.dx == 0:
            u = 0
        else:
            u = (pyxel.frame_count // 3 % 4) * 8 # From pyxel plattformer example

        pyxel.blt(self.x - 4, self.y - 4, 0, u, 0, w, 8, 0) # From pyxel plattformer example
        self.sword.draw(-1 if u>0 else 0)




class Sword:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dx = 1
        self.length = 4

    def update(self, x, y, dx):
        if dx == 0:
            self.dx = 1
        else:
            self.dx = dx

        self.x = x + self.length * self.dx / abs(self.dx)
        self.y = y

    def draw(self, extra_y = 0):
        w = self.dx / abs(self.dx) * 8
        pyxel.blt(self.x - 4, self.y - 4 + extra_y, 0, 0, 16, w, 8, 0)
