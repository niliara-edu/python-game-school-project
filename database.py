import sqlite3

connection = sqlite3.connect("./sqlite/enemies.db")
cursor = connection.cursor()

# most information taken from https://pynative.com/python-sqlite/

def start_table():

    sqlite_query = """
    drop table if exists round;
    """
    cursor.execute(sqlite_query)
    
    sqlite_query = """
    create table \
    if not exists \
    round (\
    num int(8), \
    max_enemies int(8), \
    slimes int(8), \
    moaix int(8));"""
    
    cursor.execute(sqlite_query)
    
    sqlite_query = """
    insert into round values (1, 10, 8, 2);
    """
    cursor.execute(sqlite_query)
    
    sqlite_query = """
    select * from round
    """
    
    cursor.execute(sqlite_query)
    
    
    record = cursor.fetchall()
    print("SQLite Database Version is: ", record)
    cursor.close()


def close():
    connection.close()
