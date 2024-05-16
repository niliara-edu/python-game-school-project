import pyxel
import player
import database
import modules.vector as vector
import modules.hp_bar as hp_bar
import modules.clock as clock
import modules.counter as counter


class Game:
    def ready(self, main):
        self.main = main

        self.active_enemies = []
        self.dead_enemies = []

        self.clock = clock.Clock()
        self.counter = counter.Counter()
        self.hp_bar = hp_bar.Hp_bar()

        self.round_up_text_enabled = False

        self.player = player.Player()
        self.player.ready()
        
        pyxel.load("assets/cosas.pyxres")



    def update(self):
        self.clock.timer += 1
        if self.clock.freeze_time_left > 0:
            self.update_freeze()
            return

        self.player.update()
        self.update_clock()
        self.update_entities()

        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()



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



    def update_freeze(self):
        self.clock.freeze_time_left -= 1

        if self.clock.freeze_time_left == 0:
            self.player.is_hurt = False
    

    def update_clock(self):
        if self.counter.current_enemies < self.counter.max_enemies \
        and (self.clock.timer - self.clock.delay_new_enemy_spawn) >= self.clock.last_new_enemy_spawn_time:
            self.spawn_enemy()
            self.counter.current_enemies += 1
            self.clock.last_new_enemy_spawn_time = self.clock.timer


    def spawn_enemy(self):
        instance = database.get_enemy(self.counter.current_enemies)
        instance.ready()
        self.active_enemies.append(instance)

    
    def update_entities(self):
        self.update_active_enemies()
        self.update_player_collision()
        self.update_sword_collision()
        self.update_dead_enemies()



    def update_active_enemies(self):
        for enemy in self.active_enemies:
            enemy.update()
            if enemy.has_bullets:
                for bullet in enemy.bullets:
                    self.update_bullet(enemy, bullet)


    def update_sword_collision(self):
        for enemy in self.active_enemies:
            if self.are_nearby( (self.player.sword.position.x, self.player.sword.position.y), (enemy.position.x, enemy.position.y), (self.player.sword.length, 3)):
                self.kill_enemy(enemy)

                    
    def update_player_collision(self):
        for enemy in self.active_enemies:
            if self.are_nearby( (self.player.position.x, self.player.position.y), (enemy.position.x, enemy.position.y) ):
                self.hurt_player(enemy.damage)

            if enemy.has_bullets:
                for bullet in enemy.bullets:
                    if self.are_nearby( (self.player.position.x, self.player.position.y), (bullet.position.x, bullet.position.y) ):
                        self.hurt_player(bullet.damage)

        for enemy in self.dead_enemies:
            if enemy.has_bullets:
                for bullet in enemy.bullets:
                    if self.are_nearby( (self.player.position.x, self.player.position.y), (bullet.position.x, bullet.position.y) ):
                        self.hurt_player(bullet.damage)


    def update_dead_enemies(self):
        for enemy in self.dead_enemies:
            if enemy.respawn_time <= self.clock.timer:
                self.dead_enemies.remove(enemy)
                enemy.ready()
                self.active_enemies.append(enemy)

            if enemy.has_bullets:
                for bullet in enemy.bullets:
                    self.update_bullet(enemy, bullet)



    def hurt_player(self, damage):
        if self.clock.timer < (self.clock.last_player_hurt_time + self.clock.player_hurt_time_delay):
            return

        self.player.hurt(damage)
        self.clock.freeze_time_left = 4
        self.clock.last_player_hurt_time = self.clock.timer

        self.hp_bar.update_hp(self.player.hp)

        if self.player.hp <= 0:
            self.main.end_game()


    def are_nearby(self, vec1, vec2, distance=(4,4)):
        if  vec1[0] > vec2[0] - distance[0] \
        and vec1[0] < vec2[0] + distance[0] \
        and vec1[1] > vec2[1] - distance[1] \
        and vec1[1] < vec2[1] + distance[1]:
            return True

        return False


    def kill_enemy(self, enemy):
        self.counter.score += self.counter.score_per_enemy
        self.active_enemies.remove(enemy)
        self.dead_enemies.append(enemy)

        enemy.respawn_time = self.clock.timer + self.clock.delay_enemy_respawn

        self.counter.enemies_until_next_round -= 1
        if self.counter.enemies_until_next_round == 0:
            self.round_up()


    def round_up(self):
        self.clock.freeze_time_left = self.clock.round_up_text_span
        self.round_up_text_enabled = True
        self.counter.round += 1
        round_data = database.get_round_data( self.counter.round )

        self.counter.max_enemies = round_data["max_enemies"]
        self.counter.enemies_until_next_round = round_data["enemies_until_next_round"]

        self.player.heal()
        self.hp_bar.update_hp(self.player.hp)
    


    def update_bullet(self, enemy, bullet):
        bullet.update()

        if not (0-4) < bullet.position.x < (pyxel.width+4):
            enemy.bullets.remove(bullet)




    def draw_enemies(self):
        for enemy in self.active_enemies:
            enemy.draw()
            if enemy.has_bullets:
                for bullet in enemy.bullets:
                    bullet.draw()

        for enemy in self.dead_enemies:
            if enemy.death_animation_frame < 4:
                enemy.death_animation()

            if enemy.has_bullets:
                for bullet in enemy.bullets:
                    bullet.draw()


    def draw_stats(self):
        pyxel.text(2, 2, "{0:0=2d}".format(self.counter.enemies_until_next_round), 10)
        pyxel.text(70, 10, "{0:0=3d}".format(self.counter.score), 10)
        self.hp_bar.draw()


    def draw_round_up_text(self):
        pyxel.text(35, 20, "Round up", self.clock.timer % 16)


    def draw_ground(self):
        pyxel.rect(0, 54, 100, 50, 3)

