import psycopg2


class ConectaSQL:

    def __init__(self):
        try:
            self.conexao = psycopg2.connect(user='postgres',
                                            password='admin',
                                            host='127.0.0.1',
                                            port='5432',
                                            database='numeros')
            self.conexao.autocommit = True
            self.cursor = self.conexao.cursor()

        except Exception as e:
            print('Falha ao conectar!')
            print(e)

    def consulta(self, numero):
        try:
            aux = self.cursor.execute('select * from numeros where numero = {}'.format(numero))
            aux = self.cursor.fetchall()

            return aux
        except Exception as e:
            print('Erro ao listar!')
            print(e)
