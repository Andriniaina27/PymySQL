import pymysql

class Database(object):
    __instance = None

    def __new__(cls):
        if Database.__instance is None :
            Database.__instance = super(Database, cls).__new__(cls)
        return Database.__instance
    
    def __init__(self, host="localhost", user="root", password="", database="voyage"):
        self.connexion = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connexion.cursor()

    def execute(self, query, *params):
        if self.cursor:
            self.cursor.execute(query, params)
            self.connexion.commit()

    def fetchall(self, query, *params):
        if self.cursor:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()

    def __del__(self):
        if self.cursor:
            self.cursor.close()
        if self.connexion: 
            self.connexion.close()
