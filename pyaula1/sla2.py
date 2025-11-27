import pandas as pd
# Reutilizando nosso DataFrame da aula anterior.
dados_notas = pd.DataFrame({
'aluno': ['Ana', 'Bruno', 'Carla', 'Daniel', 'Elisa', 'Fábio', 'Gabi', 'Hugo', 'Inês', 'João'],
'nota_final': [8.5, 7.0, 9.0, 5.5, 10.0, 7.0, 6.5, 8.0, 9.5, 4.0]
})
print("--- Tabela de Notas dos Alunos ---")
print(dados_notas)
print("\n" + "="*40 + "\n")

# --- Calculando a AMPLITUDE ---
# É simplesmente a diferença entre o valor máximo e o mínimo.
valor_maximo = dados_notas['nota_final'].max()
valor_minimo = dados_notas['nota_final'].min()
amplitude = valor_maximo - valor_minimo
print(f"A nota máxima foi: {valor_maximo}")
print(f"A nota mínima foi: {valor_minimo}") 
print(f"A AMPLITUDE das notas é: {amplitude:.2f}")
print("\n" + "-"*40 + "\n")

# --- Calculando a VARIÂNCIA ---
# O método .var() calcula a variância.
# Lembre-se, a unidade aqui seria "notas ao quadrado", o que é difícil de interpretar.
variancia = dados_notas['nota_final'].var()
print(f"A VARIÂNCIA das notas é: {variancia:.2f} (notas2)")

# --- Calculando o DESVIO PADRÃO ---
# O método .std() (Standard Deviation) calcula o desvio padrão.
# Esta é a medida mais importante de dispersão!
desvio_padrao = dados_notas['nota_final'].std()
media_notas = dados_notas['nota_final'].mean()
print(f"O DESVIO PADRÃO das notas é: {desvio_padrao:.2f}")
print(f"\nINTERPRETAÇÃO: Em média, uma nota qualquer da turma tende a estar a {desvio_padrao:.2f} pontos de distância da média ({media_notas:.2f}).")
print("\n" + "="*40 + "\n")