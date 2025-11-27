
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


print("Passo 1: A chamar a API 'JSONPlaceholder'...")


url_da_api = "https://jsonplaceholder.typicode.com/todos"

try:

    resposta = requests.get(url_da_api)

    resposta.raise_for_status() 
    
    print("Sucesso! A API respondeu com o código 200 (OK).")

except requests.exceptions.RequestException as e:
    print(f"Erro ao chamar a API: {e}")
    exit()


print("\nA processar a resposta JSON...")
dados_em_lista = resposta.json()
print("\nTransformar a Lista em DataFrame...")

df_tarefas = pd.DataFrame(dados_em_lista)

contagens = df_tarefas['completed'].value_counts().reset_index()
contagens.columns = ['completed', 'quantidade']
print(contagens)



print("Dados carregados e transformados em DataFrame:")
print(df_tarefas.head(10)) 
print("\n" + "="*40 + "\n")

plt.figure(figsize=(10,6))

paletaCores = ["#e40000", "#32d600" ]

sns.barplot(
    data=contagens,
    x = 'completed', y = 'quantidade',
    palette = paletaCores 
)

plt.title('Tarefas Concluídas')
plt.ylabel('Quantidade')
plt.xlabel('Concluídas')

plt.show()
