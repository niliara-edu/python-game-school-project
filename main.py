import pyxel
import player
import enemies.slime as slime
import enemies.moai as moai
import clock
import database

active_enemies = []
dead_enemies = []
oncoming_spawn_timers = []

counter = {
    "current_enemies": 0,
    "max_enemies": 4,
    "enemies_til_next_phase": 10,
}


class App:
    def __init__(self):
        pyxel.init(100, 80)
        self.player = player.Player()
        pyxel.load("assets/cosas.pyxres")
        database.start_table()

        pyxel.run(self.update, self.draw)

        
    def update(self):
        self.player.update()
        self.update_clock()
        self.update_enemies()
        
        if pyxel.btn(pyxel.KEY_Q):
            database.close()
            pyxel.quit()


    def update_clock(self):
        clock.time += 1

        if counter["current_enemies"] < counter["max_enemies"] \
        and clock.time - clock.delay_enemy_spawn >= clock.time_last_enemy_spawn:
            self.spawn_enemy()
            counter["current_enemies"] += 1
            clock.time_last_enemy_spawn = clock.time

        for procedure in oncoming_spawn_timers:
            if procedure.expected_time <= clock.time:
                oncoming_spawn_timers.remove(procedure)
                active_enemies.append(slime.Enemy())


    def spawn_enemy(self):
        active_enemies.append(slime.Enemy())
    

    def update_enemies(self):
        for enemy in active_enemies:
            enemy.update()

            if self.are_nearby( (self.player.sword.x, self.player.sword.y), (enemy.x, enemy.y) ):
                oncoming_spawn_timers.append( clock.Spawn_timer( slime.Enemy() ) )
                active_enemies.remove(enemy)
                dead_enemies.append( enemy )

                counter["enemies_til_next_phase"] -= 1
                if counter["enemies_til_next_phase"] == 0:
                    self.next_phase()


    def are_nearby(self, vec1, vec2, distance=(4,4)):
        if  vec1[0] > vec2[0] - distance[0] \
        and vec1[0] < vec2[0] + distance[0] \
        and vec1[1] > vec2[1] - distance[1] \
        and vec1[1] < vec2[1] + distance[1]:
            return True

        return False


    def next_phase(self):
        clock.text_time_left = clock.text_span

    

    def draw(self):
        pyxel.cls(0)
        self.draw_ground()
        self.draw_enemies()
        self.player.draw()
        self.draw_stats()


    def draw_enemies(self):
        for enemy in active_enemies:
            enemy.draw()
        for enemy in dead_enemies:
            if enemy.countdown < 12:
                enemy.death_anima()
            else:
                dead_enemies.remove(enemy)


    def draw_stats(self):
        pyxel.text(2, 2, "{0:0=2d}".format(counter["enemies_til_next_phase"]), 10) # double digit int from Stack Overflow

        if clock.text_time_left > 0:
            clock.text_time_left -= 1
            pyxel.text(35, 20, "Round up", pyxel.frame_count % 16) # From pyxel hello world example


    def draw_ground(self):
        pyxel.rect(0, 54, 100, 50, 3)


App()
