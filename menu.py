import pyxel


class Menu():
    def ready(self, main):
        self.main = main
        self.enter_pressed = True
        self.draw()

    def update(self):
        if pyxel.btn(pyxel.KEY_RETURN):
            if not self.enter_pressed: self.main.start_game()
        else:
            self.enter_pressed = False
            
    def draw(self):
        pyxel.cls(0)
        pyxel.text(10, 35, "Press enter to start", 9)
        pyxel.text(20, 20, "NOOB ADVENTURE", 10)
        
