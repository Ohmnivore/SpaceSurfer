import sqlite3 as sq

class DB:
    def __init__(self, name):
        self.con = None
        self.con = sq.connect(name)

        with self.con:
            cur = self.con.cursor()
            cur.execute(
            """
            CREATE TABLE History(
                Id INT PRIMARY KEY NOT NULL
                Url TEXT NOT NULL,
                Title TEXT NOT NULL,
                Time TEXT NOT NULL)
            """)
