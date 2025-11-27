# Dados do Aluno
nota1 = 5.0
nota2 = 8.0
nota3 = 9.0
# 1. Cálculo (A Lógica)
soma = nota1 + nota2 + nota3
media = soma / 3
# 2. Decisão (A Regra de Negócio)
print(f"A média final é: {media:.1f}")
if media >= 7.0:
    print("Situação: APROVADO")
else:
    print("Situação: REPROVADO")




# --- AS FERRAMENTAS (Funções) ---
def calcular_media(n1, n2, n3):
    """Apenas faz a conta matemática."""
    return (n1 + n2 + n3) / 3
def verificar_situacao(media_aluno):
    """Apenas aplica a regra da escola (Média 7)."""
    if media_aluno >= 7.0:
        return "APROVADO"
    else:
        return "REPROVADO"
# --- O PROGRAMA PRINCIPAL (Main) ---
# Agora o código fica limpo e parece uma conversa em inglês/português
if __name__ == "__main__":
# Dados
    valor_final = calcular_media(5.0, 8.0, 9.0)
    resultado = verificar_situacao(valor_final)
    print(f"A média é {valor_final:.1f} e o aluno está {resultado}")
    




import pandas as pd
# Criação dos dados
dados = {
    'Produto': ['Celular', 'Notebook', 'Tablet'],
    'Preco': [1200, 3500, 800],
    'Quantidade': [10, 5, 8]
}


df = pd.read_csv(dados) # Supondo que leu de algum lugar ou criou assim
# Lógica misturada: Calcula faturamento total
df['Total'] = df['Preco'] * df['Quantidade']
faturamento_total = df['Total'].sum()
# Mostra resultado
print("Tabela de Vendas:")
print(df)
print(f"Faturamento da Empresa: R$ {faturamento_total}")






import pandas as pd
# --- FUNÇÕES ---
def obter_dados():
    """Simula a leitura de uma planilha."""
    dados = {
        'Produto': ['Celular', 'Notebook', 'Tablet'],
        'Preco': [1200, 3500, 800],
        'Quantidade': [10, 5, 8]
    }
    return pd.DataFrame(dados)
def analisar_vendas(tabela):
    """Recebe a tabela e calcula o total."""
    # Cria a coluna nova
    tabela['Faturamento'] = tabela['Preco'] * tabela['Quantidade']
    # Calcula a soma
    total_geral = tabela['Faturamento'].sum()
    return tabela, total_geral
# --- EXECUÇÃO ---
if __name__ == "__main__":
    # 1. Pega os dados (não importa de onde vêm)
    df_bruto = obter_dados()
    # 2. Analisa (não importa quais são os dados)
    df_analisado, lucro_total = analisar_vendas(df_bruto)
    # 3. Mostra
    print(df_analisado)
    print(f"Lucro Total: R$ {lucro_total}")
