import yfinance as yf
import sqlite3
from datetime import datetime, timedelta

class InserirCotacao:

    def __init__(self):
        self.conn = sqlite3.connect('finance.db')
        self.cursor = self.conn.cursor()

    #É UMA BOA IDEIA CRIAR UMA VARIÁVEL PRA ASSUMIR O SELF., EVITANDO REPETIÇÃO EXAGERADA/BAGUNÇA
    def executar(self):
        while True:

            acao = input('Digite o nome do ticker: ').upper()
            qnt = int(input('Digite a quantidade de tickers comprados: '))
            data = input('Digite a data de compra no formato dd/mm/aa: ')

            dataform = datetime.strptime(data, "%d/%m/%y")
            datafinal = dataform + timedelta(days=1)

            preco = yf.download(f'{acao}.SA', start=dataform, end=datafinal)
            precof = float(preco['Close'][f'{acao}.SA'].dropna().iloc[0])
            total = precof*qnt

            print(acao, precof)
            print(total)

            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS savedata (
                    id INTEGER PRIMARY KEY,
                    acao TEXT NOT NULL,
                    precof FLOAT NOT NULL,
                    total FLOAT NOT NULL
                )
            ''')
            self.conn.commit()

            dados = (acao, precof, total)
            self.cursor.execute('INSERT INTO savedata (acao, precof, total) VALUES (?, ?, ?)', dados)
            self.conn.commit()

            self.cursor.execute('SELECT * FROM savedata')
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)

            quebra = input('Deseja continuar?(S/N) ')
            if quebra != "S":
                break
            else:
                continue

