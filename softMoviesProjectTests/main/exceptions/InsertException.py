class InsertException(Exception):

    def __init__(self, tabela: str, funcao: str, objeto, psycopg_log: str):
        super().__init__("INSERIR", tabela, funcao, objeto, psycopg_log)
