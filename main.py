import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.player = Player()
        pyxel.run(self.update, self.draw)

    def update(self):
        self.player.update()
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        self.player.draw()
        pyxel.rect(0, 100, 160, 20, 9)



class Player:
    def __init__(self):
        self.x = 20
        self.y = 0
        self.dx = 0
        self.dxlast = 0
        self.dy = 0

        self.on_ground = False
        self.speed = 2


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
            self.y = 92
            self.on_ground = True
            self.check_jump()
            return

        self.dy = self.dy + 1.2
        self.y += self.dy

    def is_on_ground(self):
        if self.y + self.dy >= 92:
            return True
        else:
            return False

    def check_jump(self):
        if pyxel.btn(pyxel.KEY_UP):
            self.dy = -8
            self.on_ground = False


    def draw(self):
        pyxel.rect(self.x, self.y, 8, 8, 10)
App()
