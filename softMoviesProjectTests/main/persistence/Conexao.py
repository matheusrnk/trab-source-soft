import psycopg2
import psycopg2 as postgres


class Conexao:
    __instance = None
    __connection = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__connection = postgres.connect(host='localhost', database='filmesDatabase',
                                                user='postgres', password="123")
        return cls.__instance

    def cursor(self):
        return self.__connection.cursor()

    def commit(self):
        try:
            self.__connection.commit()
        except psycopg2.InterfaceError as e:
            raise e

    def close(self):
        return self.__connection.close()
