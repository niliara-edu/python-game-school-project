import pyxel
import player as player_file
import enemies.slime as slime

enemies = []
dead_enemies = []
        
class App:
    def __init__(self):
        pyxel.init(100, 80)
        self.player = player_file.Player()
        pyxel.load("assets/cosas.pyxres")
        enemies.append(slime.Enemy())

        pyxel.run(self.update, self.draw)

        

    def update(self):
        self.player.update()
        for enemy in enemies:
            enemy.update()

            if self.are_nearby( (self.player.sword.x, self.player.sword.y), (enemy.x, enemy.y) ):
                enemies.remove(enemy)
                dead_enemies.append(enemy)


        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()


    def are_nearby(self, vec1, vec2, distance=(4,4)):
        if  vec1[0] > vec2[0] - distance[0] \
        and vec1[0] < vec2[0] + distance[0] \
        and vec1[1] > vec2[1] - distance[1] \
        and vec1[1] < vec2[1] + distance[1]:
            return True

        return False


    def draw(self):
        pyxel.cls(0)
        self.draw_ground()

        for enemy in enemies:
            enemy.draw()
        for enemy in dead_enemies:
            if enemy.countdown < 12:
                print(enemy.countdown)
                enemy.death_anima()
            else:
                dead_enemies.remove(enemy)

        self.player.draw()


    def draw_ground(self):
        pyxel.rect(0, 54, 100, 50, 6)


App()
