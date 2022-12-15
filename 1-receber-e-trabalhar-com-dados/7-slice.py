teclado = "teclado"
print(teclado[2])

print(teclado.index("a"))

print(teclado[teclado.index("a")])

esporte = "futebol tenis corrida vôlei basquetebol"
print(esporte[-1])
print(esporte.rindex("t"))

link = "facebook.com/devaprender"
print(link[0])
print(link[-1])
print(link[0:5])
print(link[0:])
print(link[-5:])
print(link[5:])
print(link[:-5])

# DESAFIO
# 1 - Encontre o índice de 'o' dentro da variável biblioteca
biblioteca = 'Biblioteca'
print(biblioteca[5])

# 2 - Usando a frase
frase = 'Desenvolvimento De Aplicações'
# Imprima apenas 'De Aplicações'
print(frase[-13:])
