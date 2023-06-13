class UpdateException(Exception):

    def __init__(self, tabela: str, funcao: str, objeto, psycopg_log: str):
        super().__init__("ATUALIZAR", tabela, funcao, objeto, psycopg_log)
