import sqlite3

connection = sqlite3.connect('spr_v1.1.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, first_name text, last_name text," \
               "age Integer,email String, phone text,password text,locality_id Integer,city_id Integer,created_date " \
               "text,updated_date text) "
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS city_master (id INTEGER PRIMARY KEY, name text,created_date text," \
               "updated_date text) "
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS locality_master (id INTEGER PRIMARY KEY, name text,created_date text," \
               "updated_date text) "
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS state_master (id INTEGER PRIMARY KEY, name text,created_date text," \
               "updated_date text) "
cursor.execute(create_table)

connection.close()

