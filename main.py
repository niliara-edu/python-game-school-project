import pyxel
import database
import game
import menu
import end_screen

from enum import Enum
Section = Enum('Section', ['MENU', 'GAME', 'END_SCREEN', 'LEADERBOARD'])


class Main:
    def ready(self):
        pyxel.init(100, 80)
        database.start_tables()
        self.menu = menu.Menu()
        self.game = game.Game()
        self.end_screen = end_screen.End_screen()

        self.start_menu()

        pyxel.run(self.update, self.draw)


    def update(self):
        match self.section:
            case Section.MENU.value:
                self.menu.update()
            case Section.GAME.value:
                self.game.update()
                self.game.draw()
            case Section.END_SCREEN.value:
                self.end_screen.update()
                self.end_screen.draw()


    def start_menu(self):
        self.menu.ready(self)
        self.section = Section.MENU.value


    def start_game(self):
        self.game.ready(self)
        self.section = Section.GAME.value


    def end_game(self):
        self.end_screen.ready(self, self.game)
        self.section = Section.END_SCREEN.value


    def draw(self):
        ### Deleting this breaks the game, so let's not. ###
        pass




Main().ready()
