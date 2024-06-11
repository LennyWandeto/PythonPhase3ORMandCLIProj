import sqlite3

CONN = sqlite3.connect('workshop.db')
CURSOR = CONN.cursor()