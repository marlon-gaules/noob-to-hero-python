from datetime import datetime

print(datetime.now())

print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)

# criando uma data
lancamento_app = datetime(2021, 5, 28)
print(lancamento_app)

# lançamento do meu app
data_de_lancamento = datetime.strptime(
    input("Quando devemos lançar o aplicativo?"), "%d/%m/%Y")
print(type(data_de_lancamento))

# quanto tempo possuo até a data de lançamento?
data_atual = datetime.now()
prazo = data_de_lancamento - data_atual
print(prazo.days)

# Desafio
# Calcule quantos dias faltam até seu aniversário!
aniversario2 = datetime(2023, 6, 15)

data_hoje = datetime.now()

quantos_dias = aniversario2 - data_hoje
print(quantos_dias)
