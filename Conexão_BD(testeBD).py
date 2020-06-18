"""
Banco de dados local criado testeBD - MySQL v8.0
"""
from Ferramentas import *
import pyodbc

linha()
try:
    conn = pyodbc.connect('Driver={MySQL ODBC 8.0 ANSI Driver};'
                          'Server=localhost;'
                          'Database=testebd;'
                          'UID=root;'
                          'PWD=123456;')
except Exception as erro:
    print(f'Erro na conexão: {erro}')
else:
    print('Conexão feita com êxito')


def consultaRegistro(conn):
    print('LENDO INFORMAÇÕES DO BANCO: ')
    cursor = conn.cursor()
    cursor.execute('select * from cliente')
    for linha in cursor:
        print(f'Linha: {linha}')
    cursor.close()
    print()


def criarRegistro(conn):
    print('Criando registro.')
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO CLIENTE VALUES(
    'Maria',
    'F',
    'maria@google.com.br',
    12345678,
    'NULL',
    'Carlos atayde - Centro - Montes Claros - MG')""")
    conn.commit()
    cursor.close()


def deleteRegistro(conn):
    print('DELETANDO REGISTRO:')
    cursor = conn.cursor()
    cursor.execute("""
    DELETE FROM CLIENTE 
    WHERE NOME = 'JORGE';
    """)
    conn.commit()
    cursor.close()


consultaRegistro(conn)
