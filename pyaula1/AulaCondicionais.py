# tem = int(input ("Garçom, tem pitu??? \n1.Sim\n2.Não"))

# if tem == 1:
#     andouHoje = int(input("Trás \nGarçom, meu amor andou aqui hoje?\n1.Sim\n2.Não"))

#     if andouHoje == 2:
#         print("Não? Onde anda o meu amoooor, irráaaaaa")
#     elif andouHoje == 1:
#         print("Dahora em")        
# if tem == 2:
#     print("Vixe, ent n trás não")

import pandas as pd
print("--- Demonstração do Laço 'for' ---")
lista_de_produtos = ['Café', 'Açúcar', 'Leite', 'Pão']
# 'item' é uma variável temporária que assume o valor de cada item da lista,
# um de cada vez, a cada "volta" do laço.
for item in lista_de_produtos:
    print(f"Processando o produto: {item}")
    print("\n--- Laço 'for' com números ---")
    # range(1, 6) cria uma sequência de números de 1 a 5
for numero in range(1, 6):
    print(f"O número da vez é: {numero}")
    print("\n" + "="*50 + "\n")