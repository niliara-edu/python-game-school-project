import sqlite3
import os


import enemies.slime as slime
import enemies.bird as bird
import enemies.ghost as ghost
import enemies.moai as moai

connection = sqlite3.connect("./sqlite/enemies.db")
cursor = connection.cursor()


if not os.path.exists("./sqlite/"):
    os.makedirs("./sqlite/")



def start_tables():
    start_rounds_table()
    start_enemies_table()
    start_highscores_table()


def start_rounds_table():

    cursor.execute( """
    drop table if exists round;
    """)
    
    cursor.execute( """
    create table 
    if not exists 
    round (
        max_enemies int(8), 
        enemies_until_next_round int(8)
    );
    """)

    cursor.execute( """
    insert into round (max_enemies, enemies_until_next_round) values
    (7, 15),
    (11, 20),
    (14, 25)
    ;
    """ )


def start_enemies_table():
    cursor.execute( "drop table if exists enemies;" )
    cursor.execute( "drop table if exists enemy_index;" )

    cursor.execute( """
    create table if not exists enemies (
        enemy_name varchar(10)
    )
    """ )

    cursor.execute( """
    create table if not exists enemy_index (
        enemy_name varchar(10)
    )
    """ )

    cursor.execute( """
    insert into enemies (enemy_name) values
        ("Slime"),
        ("Slime"),
        ("Slime"),
        ("Slime"),

        ("Bird"),
        ("Slime"),
        ("Bird"),

        ("Moai"),
        ("Slime"),
        ("Slime"),
        ("Bird"),

        ("Ghost"),
        ("Moai"),
        ("Slime"),

        ("Bird");
    """ )


    cursor.execute( """
    insert into enemy_index (enemy_name) values
        ("Slime"),
        ("Bird"),
        ("Ghost"),
        ("Moai"),
        ("Monkey");
    """ )


def get_round_data(round_num):
    result = cursor.execute( f"""
    select max_enemies, enemies_until_next_round from round
    where rowid = {round_num};
    """ ).fetchone()

    return {
        "max_enemies": result[0],
        "enemies_until_next_round": result[1]
    }


def get_enemy(enemy_num):
    result = cursor.execute( f"""
    select enemy_index.rowid
    from enemy_index
    inner join enemies on enemies.enemy_name = enemy_index.enemy_name
    where enemies.rowid = {enemy_num+1};
    """).fetchone()

    match result[0]:
        case 1: return slime.Enemy()
        case 2: return bird.Enemy()
        case 3: return ghost.Enemy()
        case 4: return moai.Enemy()
        case 5: return moai.Enemy()

def start_highscores_table():
    cursor.execute("""
    create table if not exists highscores (
        username varchar(8),
        score int(32),
        time int(32)
    )
    """)

def test_highscores():
    return [["me", 200, 1119], ["notme", 200, 1120]]


def save_score(username, score, time):
    cursor.execute( f"""
    insert into highscores (username, score, time) values
    ("{username}", {score}, {time});
    """)
    #30fps
