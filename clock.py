time = 0
delay_enemy_spawn = 100
delay_enemy_respawn = 30
time_last_enemy_spawn = -200

class Spawn_timer:
    def __init__(self, entity):
        self.entity = entity
        self.expected_time = time + delay_enemy_respawn