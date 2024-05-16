import pyxel
import database


class End_screen():
    def ready(self, main, game):
        self.main = main
        self.game = game
        self.section_user = False
        self.char_removed = False
        self.keys_pressed_list = ["S"]
        self.char_limit = 8
        self.key_pressed = True

        self.draw_restart_screen()

        
    def update(self):
        if self.section_user:
            self.input_key()
            return
        
        if pyxel.btn(pyxel.KEY_R):
            self.main.start_game()
        if pyxel.btn(pyxel.KEY_S):
            self.section_user = True
            self.username = ""
            self.last_key="S"


    def draw(self):
        if self.section_user:
            self.draw_username_input()
        else:
            self.draw_restart_screen()
            

    def draw_restart_screen(self):
        pyxel.cls(0)

        pyxel.text(10, 20, "RESTART?", 9)
        pyxel.text(24, 40, "R", 9)
        pyxel.text(70, 20, "SAVE", 10)
        pyxel.text(76, 40, 'S', 10)


    def input_key(self):
        self.key_pressed = False
        self.last_keys_pressed_list = self.keys_pressed_list
        self.keys_pressed_list = []
        if pyxel.btn(pyxel.KEY_Q): self.add_char('Q')
        if pyxel.btn(pyxel.KEY_W): self.add_char('W')
        if pyxel.btn(pyxel.KEY_E): self.add_char('E')
        if pyxel.btn(pyxel.KEY_R): self.add_char('R')
        if pyxel.btn(pyxel.KEY_T): self.add_char('T')
        if pyxel.btn(pyxel.KEY_Y): self.add_char('Y')
        if pyxel.btn(pyxel.KEY_U): self.add_char('U')
        if pyxel.btn(pyxel.KEY_I): self.add_char('I')
        if pyxel.btn(pyxel.KEY_O): self.add_char('O')
        if pyxel.btn(pyxel.KEY_P): self.add_char('P')
        if pyxel.btn(pyxel.KEY_A): self.add_char('A')
        if pyxel.btn(pyxel.KEY_S): self.add_char('S')
        if pyxel.btn(pyxel.KEY_D): self.add_char('D')
        if pyxel.btn(pyxel.KEY_F): self.add_char('F')
        if pyxel.btn(pyxel.KEY_G): self.add_char('G')
        if pyxel.btn(pyxel.KEY_H): self.add_char('H')
        if pyxel.btn(pyxel.KEY_J): self.add_char('J')
        if pyxel.btn(pyxel.KEY_K): self.add_char('K')
        if pyxel.btn(pyxel.KEY_L): self.add_char('L')
        if pyxel.btn(pyxel.KEY_Z): self.add_char('Z')
        if pyxel.btn(pyxel.KEY_X): self.add_char('X')
        if pyxel.btn(pyxel.KEY_C): self.add_char('C')
        if pyxel.btn(pyxel.KEY_V): self.add_char('V')
        if pyxel.btn(pyxel.KEY_B): self.add_char('B')
        if pyxel.btn(pyxel.KEY_N): self.add_char('N')
        if pyxel.btn(pyxel.KEY_M): self.add_char('M')
        if pyxel.btn(pyxel.KEY_SPACE): self.add_char(' ')

        if pyxel.btn(pyxel.KEY_BACKSPACE): self.remove_char()
        else: self.char_removed = False

        if pyxel.btn(pyxel.KEY_RETURN): self.save_data()


    def add_char(self, c):
        self.key_pressed = True
        if len(self.username) >= self.char_limit:
            return

        self.keys_pressed_list.append(c)
        if not (c in self.last_keys_pressed_list):
            self.username += c
            self.last_key = c


    def remove_char(self):
        self.key_pressed = True
        if not self.char_removed:
            self.username = self.username[:-1]
            self.char_removed = True


    def save_data(self):
        database.save_score(
            username = self.username,
            score = self.game.counter.score,
            time = self.game.clock.timer
        )

        self.main.start_menu()

        
    def draw_username_input(self):
        if self.key_pressed:
            pyxel.cls(0)
            pyxel.text(10, 20, "INPUT USERNAME:", 9)
            pyxel.text(10, 30, self.username, 9)
        

