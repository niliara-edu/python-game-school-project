import pyxel
import player
import enemies.slime as slime
import clock
import database


class Game:
    def __init__(self, main):
        self.main = main

        self.active_enemies = []
        self.dead_enemies = []

        self.clock = clock.Clock()
        self.counter = clock.Counter()

        self.player = player.Player()
        pyxel.load("assets/cosas.pyxres")


        
    def update(self):
        self.clock.timer += 1
        if self.clock.round_up_text_time_left > 0:
            return

        self.player.update()
        self.update_clock()
        self.update_entities()
        


    def update_clock(self):
        if self.counter.current_enemies < self.counter.max_enemies \
        and (self.clock.timer - self.clock.delay_new_enemy_spawn) >= self.clock.time_last_new_enemy_spawn:
            self.spawn_enemy()
            self.counter.current_enemies += 1
            self.clock.time_last_new_enemy_spawn = self.clock.timer


    def spawn_enemy(self):
        self.active_enemies.append( slime.Enemy() )

        #try:
        #    self.active_enemies.append( stage1_enemies[self.counter.current_enemies] )
        #except:
        #    self.active_enemies.append( slime.Enemy() )
            
    
    def update_entities(self):
        self.update_active_enemies()
        self.update_player_collision()
        self.update_sword_collision()
        self.update_dead_enemies()


    def update_active_enemies(self):
        for enemy in self.active_enemies:
            enemy.update()


    def update_sword_collision(self):
        for enemy in self.active_enemies:
            if self.are_nearby( (self.player.sword.position.x, self.player.sword.position.y), (enemy.position.x, enemy.position.y), (4,3)):
                self.active_enemies.remove(enemy)
                enemy.respawn_time = self.clock.timer + self.clock.delay_enemy_respawn
                self.dead_enemies.append( enemy )

                self.counter.enemies_until_next_round -= 1
                if self.counter.enemies_until_next_round == 0:
                    self.round_up()

                    
    def update_player_collision(self):
        for enemy in self.active_enemies:
            if self.are_nearby( (self.player.position.x, self.player.position.y), (enemy.position.x, enemy.position.y) ):
                self.main.start_menu()


    def update_dead_enemies(self):
        for enemy in self.dead_enemies:
            if enemy.respawn_time <= self.clock.timer:
                self.dead_enemies.remove(enemy)
                enemy.__init__()
                self.active_enemies.append(enemy)


    def are_nearby(self, vec1, vec2, distance=(4,4)):
        if  vec1[0] > vec2[0] - distance[0] \
        and vec1[0] < vec2[0] + distance[0] \
        and vec1[1] > vec2[1] - distance[1] \
        and vec1[1] < vec2[1] + distance[1]:
            return True

        return False


    def round_up(self):
        self.clock.round_up_text_time_left = self.clock.round_up_text_span
        self.counter.round += 1
        round_data = database.get_round_data( self.counter.round )

        self.counter.max_enemies = round_data["max_enemies"]
        self.counter.enemies_until_next_round = round_data["enemies_until_next_round"]
    


    def draw(self):
        if self.clock.round_up_text_time_left > 0:
            self.draw_round_up_text()
            self.clock.round_up_text_time_left -= 1
            return

        pyxel.cls(0)
        self.draw_ground()
        self.draw_enemies()
        self.player.draw()
        self.draw_stats()


    def draw_enemies(self):
        for enemy in self.active_enemies:
            enemy.draw()

        for enemy in self.dead_enemies:
            if enemy.death_anima_frame < 12:
                enemy.death_anima()


    def draw_stats(self):
        pyxel.text(2, 2, "{0:0=2d}".format(self.counter.enemies_until_next_round), 10) # double digit int from Stack Overflow


    def draw_round_up_text(self):
        pyxel.text(35, 20, "Round up", self.clock.timer % 16) # From pyxel hello world example


    def draw_ground(self):
        pyxel.rect(0, 54, 100, 50, 3)

