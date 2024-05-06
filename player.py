import pyxel

class Player:
    def __init__(self):
        self.x = 20
        self.y = 0
        self.dx = 0
        self.dy = 0

        self.dxlast = 0
        self.on_ground = False

        self.speed = 1
        self.gravity = 1.2
        self.jump_force = 8
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
        if self.margin < new_x < pyxel.width - self.margin - 8:
            return False

        return True

    def check_jump(self):
        if pyxel.btn(pyxel.KEY_UP):
            self.dy = -self.jump_force
            self.on_ground = False


    def draw(self):
        w = 8 if self.dxlast >= 0 else -8

        if not self.on_ground:
            if self.dy < 0:
                u = 16
            if self.dy > 0:
                u = 24

        elif self.dx == 0:
            u = 0
        else:
            u = (pyxel.frame_count // 3 % 4) * 8

        pyxel.blt(self.x, self.y, 0, u, 0, w, 8, 0)
        self.sword.draw()




class Sword:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dx = 1
        self.length = 8

    def update(self, x, y, dx):
        if dx == 0:
            dx = 1

        self.x = x + self.length * dx / abs(dx)
        self.y = y + 3

    def draw(self):
        pyxel.rect(self.x, self.y, self.length, 2, 6)
