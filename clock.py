import pyxel

class Clock():
    delay_new_enemy_spawn = 120
    last_new_enemy_spawn_time = -200

    delay_enemy_respawn = 30
    round_up_text_span = 16
    freeze_time_left = 0

    player_hurt_time_delay = 20
    last_player_hurt_time = 0
    
    timer = 0


class Counter():
    current_enemies = 0
    max_enemies = 3
    enemies_until_next_round = 5
    round = 0
    score = 0

