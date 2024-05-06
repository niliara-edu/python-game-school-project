import pyxel
import player as player_file

class App:
    def __init__(self):
        pyxel.init(100, 100)
        self.player = player_file.Player()
        pyxel.load("assets/cosas.pyxres")
        pyxel.run(self.update, self.draw)
        

    def update(self):
        self.player.update()

        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        self.draw_ground()
        self.player.draw()


    def draw_ground(self):
        pyxel.rect(0, 100, 160, 20, 9)


App()
