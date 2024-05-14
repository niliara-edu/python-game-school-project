import pyxel
import database
import game
import menu

from enum import Enum
Section = Enum('Section', ['MENU', 'GAME', 'END_SCREEN', 'LEADERBOARD'])


class Main:
    def __init__(self):
        pyxel.init(100, 80)
        database.start_tables()
        self.menu = menu.Menu(self)
        self.game = game.Game(self)

        self.start_menu()

        pyxel.run(self.update, self.draw)


    def update(self):
        match self.section:
            case Section.MENU.value:
                self.menu.update()
                self.menu.draw()
            case Section.GAME.value:
                self.game.update()
                self.game.draw()

        if pyxel.btn(pyxel.KEY_Q):
            database.close()
            pyxel.quit()


    def start_menu(self):
        self.menu.__init__(self)
        self.section = Section.MENU.value


    def start_game(self):
        self.game.__init__(self)
        self.section = Section.GAME.value


    def draw(self):
        ### Deleting this breaks the game, so let's not. ###
        pass




Main()
