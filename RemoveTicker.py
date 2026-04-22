import sqlite3
from InsertTicker import InserirCotacao

def executar(self):
    sqlite3.connect('finance.db')

    self.cursor.execute('SELECT * FROM savedata')
    rows = self.cursor.fetchall()
    for row in rows:
        print(row)