import pyxel


class Menu():
    def __init__(self, main):
        self.main = main

    def update(self):
        if pyxel.btn(pyxel.KEY_SPACE):
            self.main.start_game()
            
    def draw(self):
        pyxel.text(5, 20, "Press space to start", 9)
