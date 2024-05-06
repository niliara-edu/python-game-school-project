import pyxel
import player as player_file
import enemy as enemy_file

enemies = []
        
class App:
    def __init__(self):
        pyxel.init(100, 80)
        self.player = player_file.Player()
        pyxel.load("assets/cosas.pyxres")
        enemies.append(enemy_file.Enemy())

        pyxel.run(self.update, self.draw)

        

    def update(self):
        self.player.update()
        for enemy in enemies:
            enemy.update()

        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        self.draw_ground()
        self.player.draw()

        for enemy in enemies:
            enemy.draw()


    def draw_ground(self):
        pyxel.rect(0, 58, 100, 50, 6)


App()
