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