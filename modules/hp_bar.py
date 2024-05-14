import pyxel
import modules.vector as vector

class Hp_bar():
    def __init__(self):
        self.position = vector.Vector(70,2)
        self.length = 25
        self.greenbar_length = 25
        self.width = 5

    def update_hp(self, hp):
        self.greenbar_length = hp/4
        
    def draw(self):
        pyxel.rect(self.position.x, self.position.y, self.length, self.width, 8)
        pyxel.rect(self.position.x, self.position.y, self.greenbar_length, self.width, 11)
        
