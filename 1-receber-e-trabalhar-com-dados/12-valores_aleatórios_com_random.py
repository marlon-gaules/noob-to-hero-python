import random

print(random.random())

print(random.uniform(4, 10))

print(random.randint(2, 8))

cores = ["verde", "vermelho", "azul"]
print(random.choice(cores))
print(random.choices(cores, k=2))

cartas_de_um_baralho = ["carta1", "carta2",
                        "carta3", "carta4"]
print(random.shuffle(cartas_de_um_baralho))
print(cartas_de_um_baralho)

# Desafios Random
# 1. Você quer simular a opção de jogar uma moeda e resultar em cara ou coroa
#   jogue as opções dentro de uma variável e depois crie um programa que imprimir 'cara' ou 'coroa' na tela
moeda = ["cara", "coroa"]
print(random.choice(moeda))

# 2. Você quer fazer um sorteio entre 4 nomes em uma lista de nomes
#   Crie uma lista com 4 nomes e sorteie um nome de dentro dessa lista e exiba na tela
nomes = ["Léo", "Marlon", "Nick", "Tina"]
print(random.choice(nomes))

# 3. você quer escolher aleatóriamente um número de 10-100
#   Imprima na tela um valor aleatório inteiro entre 10 e 100
print(random.randint(10, 100))
