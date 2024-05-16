import pyxel
import database


class Highscores():
    def ready(self, main):
        self.main = main
        self.highscores = database.get_highscores()
        self.y = 0
        self.scrolling_speed = 3
        self.enter_pressed = True
        self.draw()

    def update(self):
        if pyxel.btn(pyxel.KEY_RETURN):
            if not self.enter_pressed: self.main.start_menu()
        else:
            self.enter_pressed = False

        scrolling = 0
        if pyxel.btn(pyxel.KEY_UP):
            scrolling -= 1
        if pyxel.btn(pyxel.KEY_DOWN):
            scrolling += 1

        if scrolling != 0:
            self.y += scrolling * self.scrolling_speed
            if self.y < 0:
                self.y = 0

            self.draw()

            

    def draw(self):
        pyxel.cls(0)
        y = 20 - self.y
        pyxel.text(32, y - 10, "Highscores", 10)

        for score in self.highscores:
            pyxel.text(10, y, score[0], 9)
            pyxel.text(60, y, str(score[1]), 9)
            pyxel.text(75, y, str(score[2]), 9)
            y += 10
        
        pyxel.text(6, y, "Press ENTER to go back", 12)
