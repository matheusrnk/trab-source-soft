import unittest

import psycopg2

from main.persistence.Conexao import Conexao


class ConexaoTest(unittest.TestCase):

    def testa_igualdade_de_banco(self):
        c1 = Conexao()
        c2 = Conexao()
        self.assertEqual(c1, c2)


if __name__ == '__main__':
    unittest.main()
