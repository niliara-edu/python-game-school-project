import pyxel


class Menu():
    def __init__(self, main):
        self.main = main

    def update(self):
        if pyxel.btn(pyxel.KEY_RETURN):
            self.main.start_game()
            
    def draw(self):
        pyxel.cls(0)
        pyxel.text(10, 35, "Press enter to start", 9)
        pyxel.text(20, 20, "NOOB ADVENTURE", 10)
        
