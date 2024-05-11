import pyxel

class Clock():
    delay_enemy_spawn = 120
    delay_enemy_respawn = 30
    time_last_enemy_spawn = -200
    round_up_text_span = 16
    round_up_text_time_left = 0
    
    timer = 0


class Counter():
    current_enemies = 0
    max_enemies = 3
    enemies_until_next_round = 5
    round = 0

