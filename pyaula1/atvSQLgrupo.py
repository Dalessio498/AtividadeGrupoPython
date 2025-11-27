import mysql.connector 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

db_config = {
'host': 'localhost', 
'user': 'root', 
'password': 'senaisp', 
'database': 'logistica_db' 
}


query = """
SELECT
e.id_entregador,
e.nome,
e.tipo_veiculo,
e.zona_atuacao,
en.id_entrega,
en.id_entregador,
en.status_entrega,
en.distancia_km,
en.valor_frete,
en.data_pedido
FROM
entregadores e
INNER JOIN
entregas en ON e.id_entregador = en.id_entregador
ORDER BY
en.data_pedido;
"""

def inicio_conexao():

    try:
        conexao = mysql.connector.connect(**db_config)
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


def eficienciaVeiculo(df, colunaAgrupamento, status_sucesso="Entregue"):
    
    taxadEficiencia = (df['status_entrega'] == status_sucesso).groupby(df[colunaAgrupamento]).mean() * 100
    
    return taxadEficiencia

taxaEficiencia = eficienciaVeiculo(df, 'tipo_veiculo')
print("Taxa de eficiencia")
print(taxaEficiencia.head(3).reset_index().round(1))


def faturamentoZona(df, colunaAgrupamento, colunaValor, n_top=3):
    topFaturamento = df.groupby(colunaAgrupamento)[colunaValor].sum().sort_values(ascending=False).head(n_top)
    
    return topFaturamento

topZonas = faturamentoZona(df, 'zona_atuacao', 'valor_frete', n_top=3)
print("Maior faturamento por zona")
print(topZonas.reset_index())

# 3 

def pilotoBao(df, nome, distancia, top=3):
    pilotasso = df.groupby(nome)[distancia].sum().sort_values(ascending=False).reset_index().head(3)
    return pilotasso

pilotoBrabo = pilotoBao(df, 'nome', 'distancia_km', top=3)
print("Entregador que percorreu maior distancia")
print(pilotoBrabo.reset_index())

def graficos():

    # Cores e dados utilizados 
    cores = ["#382F32", "#FFEAF2", "#FCD9E5", "#FBC5D8", "#F1396D"]
    outrasCor = ["#ff0048", "#b13756", "#5b1023"]
    outra2Cor = ["#68b2f8", "#506ee5", "#7037cd"]

    status_counts = df['status_entrega'].value_counts()

    # ===== Gráfico 1 - Barras =====
    plt.figure(figsize=(8,5))
    sns.barplot(
        data=df,
        x='zona_atuacao',
        y='valor_frete',
        linewidth=2.5,
        palette=cores,
        errorbar=None
    )
    plt.title('Valor do Frete por Zona', fontsize=16, fontweight='bold')
    plt.xlabel("Zona de Atuação")
    plt.ylabel("Valor do Frete")    
    plt.show()

    # ===== Gráfico 2 - Pizza =====
    plt.figure(figsize=(6,6))
    plt.pie(
        status_counts,
        labels=status_counts.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=outrasCor
    )
    plt.title('Proporção de Entregas', fontsize=16, fontweight='bold')
    plt.show()

    # ===== Gráfico 3 - Barras Horizontais =====
    plt.figure(figsize=(8,5))
    sns.barplot(
        data=df,
        y='tipo_veiculo',
        x='distancia_km',
        linewidth=2.5,
        palette=outra2Cor,
        errorbar=None
    )
    plt.title('Performance por Tipo de Veículo', fontsize=16, fontweight='bold')
    plt.xlabel("Distância (km)")
    plt.ylabel("Tipo de veículo")
    plt.show()

graficos()