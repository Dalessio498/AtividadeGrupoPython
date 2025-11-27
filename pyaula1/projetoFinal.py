import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
# --- 1. CONFIGURAÇÃO ---
DB_CONFIG = {
'host': 'localhost',
'user': 'root',
'password': 'senaisp', # TODO: Aluno coloca a senha aqui
'database': 'streamvision_db'
}

query = """
SELECT
u.*,
c.*, 
v.* 
FROM Usuarios u
JOIN Visualizacoes v
ON U.id_usuario = v.id_usuario
JOIN Conteudos c
ON c.id_conteudo = v.id_conteudo;
"""

def inicio_conexao():

    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        print("Conexão bem-sucedida!")
        
        df = pd.read_sql_query(query, conexao)
        print(f"Passo 2: Dados extraídos com sucesso. {len(df)} linhas recebidas.")
        
        return df

    finally:
        if 'conexao' in locals() and conexao.is_connected():
            conexao.close()
            print("Conexão com o MySQL foi fechada.")

df = inicio_conexao()


print(df)
print("\n")
