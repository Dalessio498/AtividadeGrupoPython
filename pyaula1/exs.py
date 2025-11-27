import pandas as pd

print("-" * 25)
print("Exercicio 1 \n")

# Maneira 1

nota1 = 7.0 
nota2 = 5.5
nota3 = 8.5 

# Criação de variaveis que armazenam uma conta matematica

mediaVar = (nota1 + nota2 + nota3) / 3
somaNotas = (nota1 + nota2 + nota3)

# Prints

print(f"Media das notas: {mediaVar} (MANEIRA CONVENCIONAL)\n")

print(f"Soma das notas: {somaNotas} (MANEIRA CONVENCIONAL)\n")

#-------------------------------------------

# Maneira 2

notas = pd.DataFrame ({
    'notas': [7.0, 5.5, 8.5]
})

# Soma 
somaNumeros = notas['notas'].sum()
print(f"Soma dos numeros: {somaNumeros}\n")

# Media

mediaNumeros = notas['notas'].mean()
print(f"Media das notas {mediaNumeros}\n")

# Valor minimo e maximo

valorMax = notas ['notas'].max()
valorMin = notas ['notas'].min()

amplitudeNotas = valorMax - valorMin
print(f'Amplitude das notas: {amplitudeNotas}\n')

#----------------------------------------------
print("-" * 25)
print("Exercicio 2 \n")

# Criação de variavel com valor de texto

nome = "Marco Antonio Dalessio"

print(f"Meu nome é: {nome}")

#----------------------------------------------
print("-" * 25)
print("Exercicio 3 \n")

# Criação de variaveis que armazenam uma conta matematica

dobroNota = nota1 * 2
metadeNota = nota2 / 2

print(f"Nota 1: {nota1} dobro da nota 1: {dobroNota} \nNota 2: {nota2} metade da nota 2: {metadeNota}")
#----------------------------------------------

print("-" * 25)
print("Exercicio 4 \n")

# O "=" em python se refere a atribiuir um valor e não comparar, exemplo nome = "Nome" ou nota1 = 5

#----------------------------------------------
print("-" * 25)
print("Exercicio 5 \n")

# Criação do dataframe com 5 usuarios

notas5 = pd.DataFrame({
    'Alunos5': ['Roger', 'Orrico', 'Rafael', 'Daniel', 'Felfoldi'],
    'notaAlunos5': [7, 8, 1, 1, 10]
})

# Media

mediaNumeros5 = notas5['notaAlunos5'].mean()
print(f"Media das notas {mediaNumeros5}\n")

# Mediana

medianaNumeros5 = notas5['notaAlunos5'].median()
print(f"Mediana das notas {medianaNumeros5}\n")

# Moda

modaNumeros5 = notas5['notaAlunos5'].mode()[0]
print(f"Mediana das notas {modaNumeros5}\n")

#----------------------------------------------
print("-" * 25)
print("Exercicio 6 \n")

# Isso pode ocaionar em um cenario irrealista porque vamos supor, tenho as seguintes notas: 10, 5, 5 e 5 eu tenho uma media de notas de 5, porem com o 10, essa nota fica elevada, mesma coisa com  com notas mais baixas

print("-" * 25)
print("Exercicio 7 \n")

# Criação do dataframe com 5 usuarios

notas7 = pd.DataFrame({
    'Alunos7': ['Roger', 'Orrico', 'Rafael', 'Daniel', 'Felfoldi'],
    'notaAlunos7': [9, 8, 7, 6, 5],
    'faltas7': [1, 2, 3, 4, 5]

})

print(f"{notas7} \n")

print("-" * 25)

# Media

mediaNumeros7 = notas7['notaAlunos7'].mean()
print(f"Media das notas {mediaNumeros7}\n")

# Media

mediaFaltas7 = notas7['faltas7'].mean()
print(f"Media das faltas {mediaFaltas7}\n")

print("Pode se perceber que por ter uma presença media, tambem temos uma nota media")

#----------------------------------------------
print("-" * 25)
print("Exercicio 8 \n")

# Criação do dataframe com 10 usuarios

notas8 = pd.DataFrame({
    'Alunos8': ['Paulo Roberto', 'Willian', 'Raphael', 'Lucas Rodrigues', 'Emmilly', 'Roger', 'Orrico', 'Rafael', 'Daniel', 'Felfoldi'],
    'notaAlunos8': [9, 8, 7, 6, 5, 4, 3, 2, 1, 10],
    'faltas8': [1, 2, 3, 4, 5, 3, 2, 4, 5, 1]
})
print(f"{notas8} \n")
print("-" * 25)

# Maximo e minimo

valorMax8 = notas8 ['notaAlunos8'].max()
print(f"Valor maximo {valorMax8} \n")

valorMin8 = notas8 ['notaAlunos8'].min()
print(f"Valor minimo {valorMin8} \n")

#-------------------------------------------------

# Amplitude

amplitudeNotas8 = valorMax8 - valorMin8
print(f'Amplitude das notas: {amplitudeNotas8}\n')

# Variancia

variancia8 = notas8['notaAlunos8'].var()
print(f"A VARIÂNCIA das notas é: {variancia8:.2f} \n")

# Desvio padrão

desvioPadrao8 = notas8 ['notaAlunos8'].std()
print(f"O Desvio padrão dos milimetros é: {desvioPadrao8:.2f}")

#----------------------------------------------
print("-" * 25)
print("Exercicio 9 \n")

# Quanto maior ele ser indica que os alunos estão desalinhados em ensinamento, ja se for algo parecido, esta tudo ok!

print("-" * 25)
print("Exercicio 10 \n")

# Criação de database com 10 notas diferentes

notas10 = pd.DataFrame ({
    'Turma 1' : [4, 6, 2, 8, 9, 2, 5, 5, 10, 0],
    'Turma 2' : [7, 7, 5, 9, 1, 5, 7, 5, 7, 10]
})

# Desvio 1

desvioPadrao10 = notas10 ['Turma 1'].std()
print(f"O Desvio padrão da turma 1 é: {desvioPadrao10:.2f} \n")

# Desvio 2

desvioPadrao10 = notas10 ['Turma 2'].std()
print(f"O Desvio padrão da turma 2 é: {desvioPadrao10:.2f} \n <--- A turma 2 apresenta menor Desvio padrão")

#----------------------------------------------
print("-" * 25)
print("Exercicio 11 \n")

# Criação de database com 10 notas diferentes

maquinasMm = pd.DataFrame ({

    'maquina_A': [50.1, 50.0, 49.9, 50.0, 49.8, 50.2, 50.0, 50.1, 49.9, 50.0],
    'maquina_B': [52.5, 47.0, 50.0, 51.5, 48.0, 46.5, 53.0, 50.5, 49.0, 52.0]
  
})

# Maquina 1

# Desvio padrão

desvioPadrao11 = maquinasMm ['maquina_A'].std()
print(f"O Desvio padrão da maquina 1 é: {desvioPadrao11:.2f}mm <----- Apresenta um melhor resultado por ser menor o Desvio padrão.\n")

# Media

mediaNumeros11 = maquinasMm['maquina_A'].mean()
print(f"Media dos parafusos {mediaNumeros11}mm \n")

#---------------------------------------------------

# Maquina 2

# Desvio padrão

desvioPadrao11 = maquinasMm ['maquina_B'].std()
print(f"O Desvio padrão da maquina 2 é: {desvioPadrao11:.2f}mm \n")

# Media

mediaNumeros11 = maquinasMm['maquina_B'].mean()
print(f"Media dos parafusos {mediaNumeros11}mm \n")

#---------------------------------------------------

print("-" * 25)
print("Exercicio 12 \n")

# Para minha pessoa, é extremamente importante o uso de bibliotecas em python, principalmente 
# o pandas, que permite manipulação calculos e muitas outras coisas que envolvem arquivos
# prinicipalmente os grandes, porque 5 notas é facil de fazer a media, ja 1000 não :D

#---------------------------------------------------

print("-" * 25)
print("Exercicio 13 \n")

# Para uso pessoal, o calculo da media de fincanças, saber com o q mais gasto, a diferença de minhas compras com std
