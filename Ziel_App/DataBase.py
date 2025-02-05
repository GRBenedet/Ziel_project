import mysql.connector

config = {'user': 'root',
          'password': '1234',
          'host': '127.0.0.1:3306',
          'database': 'ziel',
          'raise_on_warnings': True}

class Ziel_DataBase:
    def __init__(self):
        self.db = mysql.connector.connect(**config)
        self.c = self.db.cursor()

    def get_rows(self):
            # a,b,c,d depence of your database structure and tables
            # use the query example below, query needs parenthesis obligated

            """query=('SELECT {} FROM {} WHERE({}='{}')'.format("a","b","c","d"))
            self.c.execute(query)
            return self.c.fetchall()"""