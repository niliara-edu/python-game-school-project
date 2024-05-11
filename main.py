import pyxel
import database
import game
import menu

########### from https://docs.python.org/3/library/enum.html ############

from enum import Enum
Stage = Enum('Stage', ['MENU', 'GAME', 'END_SCREEN', 'LEADERBOARD'])

# Other uses of enum are also taken from this website

#########################################################################


class App:
    def __init__(self):
        pyxel.init(100, 80)
        database.start_rounds_table()
        self.menu = menu.Menu(self)
        self.game = game.Game(self)

        self.start_menu()

        pyxel.run(self.update, self.draw)


    def update(self):
        match self.stage:
            case Stage.MENU.value:
                self.menu.update()
                self.menu.draw()
            case Stage.GAME.value:
                self.game.update()
                self.game.draw()

        if pyxel.btn(pyxel.KEY_Q):
            database.close()
            pyxel.quit()


    def start_menu(self):
        self.menu.__init__(self)
        self.stage = Stage.MENU.value


    def start_game(self):
        self.game.__init__(self)
        self.stage = Stage.GAME.value


    def draw(self):
        ### Deleting this breaks the game, so let's not. ###
        pass




App()
