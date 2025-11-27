#importar base de dados

import pandas as pd

dados_imoveis = pd.DataFrame({
'tipo': ['Apartamento', 'Casa', 'Apartamento', 'Casa', 'Studio', 'Casa', 'Mansão'],
'preco_milhar': [300, 450, 350, 400, 250, 500, 8000]
})

print("\n--- Preços dos Imóveis no Bairro (em milhares de R$) ---")
print(dados_imoveis)

#calcular medias

#media aritmetica
media_valor = dados_imoveis ['preco_milhar'].mean()
print(f"\n A media do valor das casas é: {media_valor:.2f} mil R$")

#mediana
mediana_valor = dados_imoveis ['preco_milhar'].median()
print(f"\n Mediana do valor das casas é: {mediana_valor:.2f} mil R$ <--- Melhor para o cliente")

#O valor da mediana é mais tipico por se tratar de numeros realistas, quando eu procuro uma casa, eu não quero saber o preço de uma mansão, e sim, de algo que eu possa pagar

