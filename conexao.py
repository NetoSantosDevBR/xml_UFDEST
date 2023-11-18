from aifc import Error
from dataclasses import replace
import pyodbc
import sys



# LENDO ARQUIVO COMAND
def ler_arquivo(caminho):

    arq = open(caminho)
    linhas = []
    if arq != None:
        linhas = arq.readlines()
        return linhas
    else:
        print('não foi possivel localizar o arquivo!')

#pegar codigo loja ativa
loja_nfe = ler_arquivo('comand.txt')
loja_nfe = loja_nfe[1].replace('LOJANFE=','')



# função de conexão ao banco com retorno console
def conexao_banco():
    # Specifying the ODBC driver, server name, database, etc. directly
    arq = ler_arquivo('comand.txt')
    caminho = str(arq[0])
    try:
        cnxn = pyodbc.connect(f'{caminho} UID=sa;PWD=XXXXXXX')
        print('\nCONECTANDO...\n')
        print("Conexão bem sucedida !")
    except:
        raise Error("Erro ao acessar dados")

        # criando cursor
    cursor = cnxn.cursor()
    return cursor

#atualizar nfe
def atualiza_nfe(numero_nfe):
    cursor = conexao_banco()
    cursor.execute(f"UPDATE NFSAIDA SET statusnfe='EM DIGITAÇÃO' WHERE loja='{loja_nfe}' and numero='{numero_nfe}' and statusnfe='Lote Recebido'"
     )
    cursor.commit()
    return cursor
