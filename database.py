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
    create table 
    if not exists 
    round (
        num int(8), 
        max_enemies int(8), 
        enemies_til_next int(8), 
    );
    """

    cursor.execute(sqlite_query)



    sqlite_query = """
    insert into round (num, max_enemies, enemies_til_next) values (1, 10, 20);
    """
    cursor.execute(sqlite_query)
    
    sqlite_query = """
    select * from round
    """
    
    cursor.execute(sqlite_query)
    
    
    record = cursor.fetchall()
    print("Round table values: ", record)
    cursor.close()


def close():
    connection.close()