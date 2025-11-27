# --- 1. IMPORTAÇÕES ---
# Importamos as bibliotecas que instalamos via 'pip'
# 'mysql.connector' é a "ponte" que permite ao Python "falar" com o MySQL
import mysql.connector
# 'pandas' é a biblioteca central de Ciência de Dados para manipular tabelas
import pandas as pd
# 'matplotlib.pyplot' é a biblioteca para criar os gráficos
import matplotlib.pyplot as plt

# --- 2. CONFIGURAÇÃO DA CONEXÃO COM O BANCO ---
print("Passo 1: Conectando ao banco de dados MySQL...")

# Criamos um dicionário Python para guardar nossas credenciais.
# É uma boa prática manter isso separado do código de conexão.
# !!! ATENÇÃO: Altere com seus dados de usuário, senha e o banco que criamos !!!
db_config = {
    'host': 'localhost',       # Geralmente 'localhost' se o banco está na sua máquina
    'user': 'root',            # Seu usuário do MySQL (padrão é 'root')
    'password': 'senaisp',  # A senha que você definiu para o usuário 'root'
    'database': 'ecommerce_db'     # O nome do banco que criamos no Passo 1
}

# --- 3. DEFINIÇÃO DA CONSULTA SQL (QUERY) ---
query = """
SELECT
    c.estado,
    p.total_pedido,
    p.data_pedido
FROM
    pedidos p
INNER JOIN
    clientes c ON p.id_cliente = c.id_cliente
ORDER BY
    p.data_pedido;
"""

# --- 4. EXTRAÇÃO DOS DADOS (Bloco try/finally) ---
try:
    # 4.1. Conectar ao banco
    conexao = mysql.connector.connect(**db_config)
    print("Conexão bem-sucedida!")

    # 4.2. Executar a query e carregar no Pandas
    df = pd.read_sql_query(query, conexao)
    print(f"Passo 2: Dados extraídos com sucesso. {len(df)} linhas recebidas.")

finally:
    # 4.3. Fechar a conexão
    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()
        print("Conexão com o MySQL foi fechada.")

# --- 5. ANÁLISE DE DADOS (Ciência de Dados com Pandas) ---
print("\n--- Iniciando Análise de Dados (Pandas) ---")
print("Dados brutos extraídos e juntados (head):")
print(df.head())
print("\n")

# 5.1. Tratamento de Dados
df['data_pedido'] = pd.to_datetime(df['data_pedido'])

# 5.2. Análise Principal: Vendas por Estado
vendas_por_estado = df.groupby('estado')['total_pedido'].sum()
vendas_por_estado = vendas_por_estado.sort_values(ascending=False)

print("--- Análise 1: Receita Total por Estado ---")
print(vendas_por_estado)
print("\n")

# 5.3. Análise Bônus: Vendas ao Longo do Tempo
vendas_por_dia = df.groupby('data_pedido')['total_pedido'].sum()

print("--- Análise 2: Receita Total por Dia ---")
print(vendas_por_dia)
print("\n")

# --- 6. VISUALIZAÇÃO (Matplotlib) ---
print("Passo 3: Gerando visualizações...")

# 6.1. Gráfico 1: Vendas por Estado (Barras)
vendas_por_estado.plot(
    kind='bar',
    title='Receita Total por Estado'
)
plt.ylabel("Receita Total (R$)")
plt.xlabel("Estado (UF)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 6.2. Gráfico 2: Vendas ao Longo do Tempo (Linhas)
vendas_por_dia.plot(
    kind='line',
    title='Evolução da Receita Diária',
    marker='o'
)
plt.ylabel("Receita (R$)")
plt.xlabel("Data do Pedido")
plt.grid(True)
plt.tight_layout()
plt.show()

print("Projeto concluído!")
