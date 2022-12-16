frase = "Olá, bem-vindo a este treinamento!"
print(frase.split())
print(frase.split(","))
print(frase.split("-"))

nomes = "Jhonatan, Rafael, Carol, Amanda,Jeferson"
print(nomes.split())
print(nomes.split(","))

hashtags = "music #guitar #gamer #coder #python"
print(hashtags.split())
print(hashtags.split("#"))
print(hashtags.split("#", 3))

hashtags_separadas_por_espaco = hashtags.split(" ")
print(hashtags_separadas_por_espaco)
print(",".join(hashtags_separadas_por_espaco))
print(".".join(hashtags_separadas_por_espaco))
print(" ".join(hashtags_separadas_por_espaco))

# ​Desafio 1: Transforme a frase1 em uma lista de palavras e guarde o resultado em uma variável chamada palavras1
# Desafio 2: Transforme a frase2 em uma lista de palavras e guarde o resultado em uma variável chamada palavras2
# Desafio 3: Pegue o palavras1 e transforme elas no seguinte string: "Desafio,manipulação,de,strings". Imprima o resultado no console.
# Desafio 4: Pegue o palavras2 e transforme elas no seguinte string: frase2 = "jhonatan & rafael & carol & camilla". Imprima o resultado no console.
frase1 = 'Desafio manipulação de strings'
frase2 = 'jhonatan,rafael,carol,camilla'

palavras1 = frase1.split(" ")
palavras2 = frase2.split(",")
print(",".join(palavras1))
print(" & ".join(palavras2))
