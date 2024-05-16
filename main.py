import pyxel
import database
import scenes.game as game
import scenes.menu as menu
import scenes.end_screen as end_screen
import scenes.highscores as highscores

from enum import Enum
Scene = Enum('Scene', ['MENU', 'GAME', 'END_SCREEN', 'HIGHSCORES'])


class Main:
    def ready(self):
        pyxel.init(100, 80)
        database.start_tables()
        self.menu = menu.Menu()
        self.game = game.Game()
        self.end_screen = end_screen.End_screen()
        self.highscores = highscores.Highscores()

        self.start_menu()

        pyxel.run(self.update, self.draw)


    def update(self):
        match self.scene:
            case Scene.MENU.value:
                self.menu.update()
            case Scene.GAME.value:
                self.game.update()
                self.game.draw()
            case Scene.END_SCREEN.value:
                self.end_screen.update()
                self.end_screen.draw()
            case Scene.HIGHSCORES.value:
                self.highscores.update()


    def start_menu(self):
        self.menu.ready(self)
        self.scene = Scene.MENU.value


    def start_game(self):
        self.game.ready(self)
        self.scene = Scene.GAME.value


    def end_game(self):
        self.end_screen.ready(self, self.game)
        self.scene = Scene.END_SCREEN.value


    def show_highscores(self):
        self.highscores.ready(self)
        self.scene = Scene.HIGHSCORES.value
        

    def draw(self):
        ### Deleting this breaks the game, so let's not. ###
        pass




Main().ready()
