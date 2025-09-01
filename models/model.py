# from .database import Database


import pymysql

class Database():
    __instance = None

    def __new__(cls):
        if Database.__instance is None :
            Database.__instance = super(Database, cls).__new__(cls)
        return Database.__instance
    
    def __init__(self):
        if not hasattr(self, "connexion"):
            self.connexion = pymysql.connect(
                host="localhost",
                user="root",
                password="",
                database="voyage"
            )
            self.cursor = self.connexion.cursor()

class Model():


    @classmethod
    def getById(cls, id):
        table = cls.__name__.lower()
        pk = "id_" + table
        query = f"SELECT * FROM {table} WHERE {pk} = %s"
        base = Database()
        base.cursor.execute(query, (id,))
        return base.cursor.fetchone()
    
    @classmethod
    def getAll(cls):
        table = cls.__name__.lower()
        query = f"SELECT * FROM {table}"
        base = Database()
        base.cursor.execute(query)
        return base.cursor.fetchall()
    
    @classmethod
    def count(cls):
        table = cls.__name__.lower()
        query = f"SELECT COUNT(*) FROM {table}"
        base = Database()
        base.cursor.execute(query)
        return base.cursor.fetchone()