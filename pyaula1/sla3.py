# --- IMPORTAÇÕES ---
# Importa a biblioteca pandas e a apelida de 'pd'.
# O pandas é a principal ferramenta para manipulação e análise de dados.
import pandas as pd
# Importa o submódulo 'pyplot' da biblioteca 'matplotlib' e o apelida de 'plt'.
# O matplotlib é usado para criar gráficos e visualizações.
import matplotlib.pyplot as plt # Para o gráfico final
# --- TAREFA 1: CRIAR NOSSOS DADOS NOVOS ---
# Aqui, em vez de ler um Excel, estamos criando os dados do zero.
# 1. Dados da "Planilha A" (Nossos Pedidos)
# Criamos um dicionário Python. As chaves ('id_pedido', 'id_produto'...)
# serão os nomes das colunas.
dados_pedidos = {
'id_pedido': [101, 102, 103, 104, 105, 106],
'id_produto': [3, 1, 2, 1, 3, 2], # Note que os IDs de produto se repetem
'valor_total': [150.00, 4500.00, 80.00, 4800.00, 160.00, 90.00]
}
# Usamos o construtor pd.DataFrame() para converter nosso dicionário
# em um DataFrame (uma tabela) do pandas.
df_pedidos = pd.DataFrame(dados_pedidos)
# 2. Dados da "Planilha B" (Nosso Cadastro de Produtos)
# Criamos um segundo dicionário para simular outra planilha.
# Esta tabela servirá como um "cadastro" ou "tabela de consulta".
dados_produtos = {
'id_produto': [1, 2, 3], # Chave única
'nome_produto': ['Notebook G10', 'Mouse Óptico', 'Teclado Mecânico'],
'categoria': ['Eletrônico', 'Periférico', 'Periférico']
}
# Convertemos o segundo dicionário em outro DataFrame.
df_produtos = pd.DataFrame(dados_produtos)

# Apenas imprimimos os DataFrames que acabamos de criar para ver como eles são.
print("--- 1. Nossos DataFrames Separados ---")
print("Planilha de Pedidos:")
print(df_pedidos)
print("\nPlanilha de Cadastro de Produtos:")
print(df_produtos)
print("\n" + "="*40 + "\n") # Imprime uma linha de "=" para separar visualmente

# --- TAREFA 2: USANDO FUNÇÕES PYTHON (.apply) ---
# (A "particularidade" do Python para criar lógica customizada)
# Problema: Queremos classificar cada pedido como 'Prioritário' (se > R$ 1000)
# ou 'Normal' (se <= R$ 1000).
# 1. Definimos a função Python "pura"
# Usamos 'def' para criar uma função chamada 'classificar_prioridade'.
# Ela espera receber um argumento, que chamamos de 'valor'.
def classificar_prioridade(valor):
#"""Se o valor for maior que 1000, retorna 'Prioritário', senão 'Normal'."""
# Lógica 'if/else' padrão do Python
    if valor > 1000:
        return 'Prioritário'
    else:
        return 'Normal'
# 2. Usamos o .apply() para aplicar essa função
# Criamos uma NOVA coluna em 'df_pedidos' chamada 'Prioridade'.
# O conteúdo dessa coluna será o resultado de:
# - Pegar a coluna 'valor_total' (df_pedidos['valor_total'])
# - Usar o método .apply() nela
# - Passar nossa função (classificar_prioridade) como argumento.
# O pandas vai "chamar" essa função para cada linha da coluna 'valor_total'.
df_pedidos['Prioridade'] = df_pedidos['valor_total'].apply(classificar_prioridade)
# Imprime o DataFrame de pedidos atualizado para vermos a nova coluna
print("--- 2. Pedidos com a Prioridade (após .apply()) ---")
print(df_pedidos)
print("\n" + "="*40 + "\n")