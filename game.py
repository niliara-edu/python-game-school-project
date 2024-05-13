import pyxel
import player
import enemies.slime as slime
import enemies.bird as bird
import enemies.ghost as ghost
import clock
import database
import modules.vector as vector
import modules.hp_bar as hp_bar


class Game:
    def __init__(self, main):
        self.main = main

        self.active_enemies = []
        self.dead_enemies = []

        self.clock = clock.Clock()
        self.counter = clock.Counter()

        self.round_up_text_enabled = False

        self.player = player.Player()
        self.hp_bar = hp_bar.Hp_bar()
        pyxel.load("assets/cosas.pyxres")


        
    def update(self):
        self.clock.timer += 1
        if self.clock.freeze_time_left > 0:
            self.clock.freeze_time_left -= 1
            return

        self.player.update()
        self.update_clock()
        self.update_entities()
        


    def update_clock(self):
        if self.counter.current_enemies < self.counter.max_enemies \
        and (self.clock.timer - self.clock.delay_new_enemy_spawn) >= self.clock.last_new_enemy_spawn_time:
            self.spawn_enemy()
            self.counter.current_enemies += 1
            self.clock.last_new_enemy_spawn_time = self.clock.timer

    def spawn_enemy(self):
        self.active_enemies.append( slime.Enemy() )
        self.active_enemies.append( bird.Enemy() )

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
            if self.are_nearby( (self.player.sword.position.x, self.player.sword.position.y), (enemy.position.x, enemy.position.y), (self.player.sword.length, 3)):
                self.active_enemies.remove(enemy)
                enemy.respawn_time = self.clock.timer + self.clock.delay_enemy_respawn
                self.dead_enemies.append( enemy )

                self.counter.enemies_until_next_round -= 1
                if self.counter.enemies_until_next_round == 0:
                    self.round_up()

                    
    def update_player_collision(self):
        for enemy in self.active_enemies:
            if self.are_nearby( (self.player.position.x, self.player.position.y), (enemy.position.x, enemy.position.y) ):
                self.hurt_player()
                self.hp_bar.update_hp(self.player.hp)

    def hurt_player(self):
        if self.clock.timer < (self.clock.last_player_hurt_time + self.clock.player_hurt_time_delay):
            return

        self.player.hurt()
        self.clock.freeze_time_left = 4
        self.clock.last_player_hurt_time = self.clock.timer

        if self.player.hp <= 0:
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
        self.clock.freeze_time_left = self.clock.round_up_text_span
        self.round_up_text_enabled = True
        self.counter.round += 1
        round_data = database.get_round_data( self.counter.round )

        self.counter.max_enemies = round_data["max_enemies"]
        self.counter.enemies_until_next_round = round_data["enemies_until_next_round"]
    


    def draw(self):
        if self.round_up_text_enabled:
            self.draw_round_up_text()
            if self.clock.freeze_time_left == 0:
                self.round_up_text_enabled = False
            return


        pyxel.cls(0)
        self.draw_stats()
        self.draw_ground()
        self.draw_enemies()
        self.player.draw()

        if self.player.is_hurt and (self.clock.freeze_time_left == 0):
            self.player.is_hurt = False



    def draw_enemies(self):
        for enemy in self.active_enemies:
            enemy.draw()

        for enemy in self.dead_enemies:
            if enemy.death_animation_frame < 4:
                enemy.death_animation()


    def draw_stats(self):
        pyxel.text(2, 2, "{0:0=2d}".format(self.counter.enemies_until_next_round), 10) # double digit int from Stack Overflow
        self.hp_bar.draw()


    def draw_round_up_text(self):
        pyxel.text(35, 20, "Round up", self.clock.timer % 16) # From pyxel hello world example


    def draw_ground(self):
        pyxel.rect(0, 54, 100, 50, 3)

