import sqlite3
import os

if not os.path.exists("./sqlite/"):
    os.makedirs("./sqlite/")

connection = sqlite3.connect("./sqlite/enemies.db")
cursor = connection.cursor()

# most information taken from https://pynative.com/python-sqlite/


def start_rounds_table():

    sqlite_query = """
    drop table if exists round;
    """
    cursor.execute(sqlite_query)
    
    sqlite_query = """
    create table 
    if not exists 
    round (
        max_enemies int(8), 
        enemies_until_next_round int(8)
    );
    """

    cursor.execute(sqlite_query)


    sqlite_query = """
    insert into round (max_enemies, enemies_until_next_round) values
    (5, 10),
    (6, 15),
    (7, 20)
    ;
    """
    cursor.execute(sqlite_query)
    

def get_round_data(round_num):
    sqlite_query = f"""
    select max_enemies, enemies_until_next_round from round
    where rowid = {round_num};
    """
    result = cursor.execute(sqlite_query).fetchone()


    return {
        "max_enemies": result[0],
        "enemies_until_next_round": result[1]
    }
    

def close():
    cursor.close()
    connection.close()
