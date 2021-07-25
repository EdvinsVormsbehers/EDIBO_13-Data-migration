import mysql.connector
import sqlite3

chinook_db = sqlite3.connect('chinook.db')
cursor_sqlite = chinook_db.cursor()

ufile = open('user.txt', 'r')
user = ufile.read()[:-1]
ufile.close()
pfile = open('password.txt', 'r')
password = pfile.read()[:-1]
pfile.close()

music_shop_db = mysql.connector.connect(
    host="localhost",
    user=user,
    password=password,
    database="music_shop"
)
cursor_mysql = music_shop_db.cursor()

cursor_sqlite.execute("SELECT name FROM sqlite_master WHERE type='table'")
chinook_tables = cursor_sqlite.fetchall()

cursor_mysql.execute("SET FOREIGN_KEY_CHECKS=0")

for table in chinook_tables:
    ch_table = table[0]
    if 'sqlite' not in ch_table:
        table_content = chinook_db.execute(f"SELECT * FROM {ch_table}")
        columns = tuple([i[0] for i in table_content.description])
        values = table_content.fetchall()

        # migrates data from chinook database into music_shop database
        insert = "".join((f"INSERT INTO {ch_table} {columns} VALUES {str(values).replace('[', '').replace(']', '').replace('None', 'Null')}").split("'", len(columns) * 2))
        cursor_mysql.execute(insert)

music_shop_db.commit()
music_shop_db.close()
