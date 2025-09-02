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
    def __close(cls):
        base = Database()
        if base.cursor :
            base.cursor.close()
        # if base.connexion:
        #     base.connexion.close()

    def __str__(self):
        chaine = ".....................................\n"
        for attr in self.__dict__.keys():
            chaine = chaine + attr + " : " +str(self.__dict__[attr]) + "\n"
        return chaine

    @classmethod
    def getById(cls, id):
        try:
            table = cls.__name__.lower()
            pk = "id_" + table
            query = f"SELECT * FROM {table} WHERE {pk} = %s"
            base = Database()
            base.cursor.execute(query, (id,))
            dict =  base.cursor.fetchone()
        except Exception as e:
            print(e)
            return[{}]
        else:
            return dict
        finally:
            cls.__close()
    
    @classmethod
    def getAll(cls):
        try:
            table = cls.__name__.lower()
            query = f"SELECT * FROM {table}"
            base = Database()
            base.cursor.execute(query)
            list = base.cursor.fetchall()
        except Exception as e:
            print(e)
            return[{}]
        else:
            return list
        finally:
            cls.__close()
            
    
    @classmethod
    def count(cls):
        table = cls.__name__.lower()
        query = f"SELECT COUNT(*) FROM {table}"
        base = Database()
        base.cursor.execute(query)
        return base.cursor.fetchone()
    
    @classmethod
    def delete(cls, id):
        try:
            table = cls.__name__.lower()
            pk = f"id_{table}"
            query = f"DELETE FROM {table} WHERE {pk} = %s"
            base = Database()
            base.cursor.execute(query, (id,))
            delete = base.connexion.commit()
        except Exception as e:
            print(e)
            return[{}]
        else:
            return delete
        finally:
            cls.__close()
    
    @classmethod
    def insert(cls, *params):
        try:
            table = cls.__name__.lower()
            param = ", ".join(["%s"] * len(params))
            query = f"INSERT INTO {table} VALUES(NULL, {param})"
            base = Database()
            base.cursor.execute(query, params)
            result =  base.connexion.commit()
        except Exception as e:
            print(e)
            return[{}]
        else:
            return result
        finally:
            cls.__close()
    
    @classmethod
    def update(cls, id, colonne, *params):
        try:
            table = cls.__name__.lower()
            pk = f"id_{table}"
            param = ", ".join([f"{col} = %s" for col in colonne])
            values = params + (id,)
            query = f"UPDATE {table} SET {param} WHERE {pk} = %s"
            base = Database()
            base.cursor.execute(query, values)
            result =  base.connexion.commit()
        except Exception as e:
            print(e)
            return[{}]
        else:
            return result
        finally:
            cls.__close()

    @classmethod
    def lastId(cls):
        try:
            table = cls.__name__.lower()
            pk = f"id_{table}"
            query = f"SELECT {pk} FROM {table} ORDER BY {pk} DESC LIMIT 1"
            base = Database()
            base.cursor.execute(query)
            result =  base.cursor.fetchone()
        except Exception as e:
            print(e)
            return[{}]
        else:
            return result
        finally:
            cls.__close()