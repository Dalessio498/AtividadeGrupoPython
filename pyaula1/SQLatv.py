import mysql.connector as sql
import pandas as pd
import time

# Passo 1 - Conectar o python ao banco de dados

# Isso vai declarar as propiedades do banco, como nome senha usuario e etc

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'senaisp',
    'database': 'plataforma_cursos_db', # Esse é o nome do schema/database
    'port': '3306'
}

# Isso vai definir qual comando do mySql ele ira executar para fazer a consulta

query = """
SELECT 
    Alunos.*,
    Matriculas.*
FROM 
    Matriculas
INNER JOIN 
    Alunos
    ON Matriculas.id_aluno = Alunos.id_aluno;
"""

    # Nesse bloco do try ele vai fazer a conexão

try:
    conexao = sql.connect(**db_config)
    print('--- Sucesso! você conseguiu se conectar ao banco de dados! ---\n')
    time.sleep(3)
    df = pd.read_sql_query(query, conexao)
    print(f"Dados extraídos com sucesso. {len(df)} linhas recebidas.\n")
    a = [1, 2, 3]
    for n in a:
        time.sleep(1)
        print('Encerrando conexão')
        
            
    # Nesse bloco do finally ele vai fechar a conexão
    
finally: 
    time.sleep(2)
    print("\n")
    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()
        print('--- ⚠️  Conexão encerrada por medida de segurança  ⚠️ ---\n')

print(df.head())

# --- EX 1: Total de receita por tipo de curso

print("Tabela de receita por categoria de curso\n")
receitaTotalCurso = df.groupby('categoria_curso')['valor_pago'].sum().reset_index()
time.sleep(2)
print(f"{receitaTotalCurso}\n")
time.sleep(1)

mediaValor = df.groupby('nome_curso')['valor_pago'].mean().reset_index()
print("Tabela de media de preço por curso\n")
time.sleep(2)
print(f"{mediaValor}\n")
time.sleep(1)

# --- EX 2: 

estadoRico = df.groupby('estado_aluno')['valor_pago'].sum().sort_values(ascending=False).reset_index().head(1)
print("Tabela de estado que gera mais receita\n")
time.sleep(2)
print(f"{estadoRico}\n")
time.sleep(1)

SPandamento = (
    
df

[   (df['estado_aluno'] == 'SP') &
    (df['status_progresso'] == 'Em Andamento')
])

print("Tabela de Alunos de São paulo em andamento\n")
time.sleep(2)
print(f"{SPandamento}\n")
time.sleep(1)


# --- EX 3:


df['data_matricula'] = pd.to_datetime(df['data_matricula'])
mes_e_ano = df['data_matricula'].dt.to_period('M')
matriculas_por_mes = mes_e_ano.value_counts().sort_index()

print("Tabela de Número de matrículas por Mês/Ano:")
print(matriculas_por_mes)

# ----------------------------------------------------------------

df['data'] = pd.to_datetime(df['data_matricula'])

vendas_por_dia = df.groupby(df['data'].dt.date)['valor_pago'].sum()

melhor_dia = vendas_por_dia.idxmax()

maior_valor = vendas_por_dia.max()

print("/n")
print("--- Melhor Dia de Vendas ---zn")
print(f"Dia: {melhor_dia}\n")
print(f"Valor Total Pago: R$ {maior_valor:,.2f}")
print("----------------------------")

# --- EX 4:

PyConcluido = (
    
df

[   (df['nome_curso'] == 'Python para Iniciantes') &
    (df['status_progresso'] == 'Concluído')
].shape[0]
)



print("Tabela de quantidade de Python para Iniciantes concluidos\n")
time.sleep(2)
print(f"{PyConcluido} Alunos\n")
time.sleep(1)

#-------------------------------------------

PyIniciante = (
    
df

[   (df['nome_curso'] == 'Python para Iniciantes') &
    (df['status_progresso'] == 'Iniciante')
].shape[0]
)



print("Tabela de quantidade de Python para Iniciantes no nivel iniciante\n")
time.sleep(2)
print(f"{PyIniciante} Alunos\n")
time.sleep(1)

