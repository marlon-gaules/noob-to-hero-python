''' 
if condicao: 
    comandos a serem executados
'''

trabalho_terminado = True
if trabalho_terminado == True:
    print("Bora dar uma saída!")
else:
    print("Não posso sair agora.")

numero_atrasos = 2
if numero_atrasos >= 3:
    print("Vá para a diretoria")
elif numero_atrasos == 2:
    print("Essa é sua segunda falta")
elif numero_atrasos == 1:
    print("Essa é sua primeira falta")
else:
    print("Pode entrar!")

'''
A velocidade máxima para essa rua é 50km
* Cruzou entre 51km a 60Km, levou multa de 2 pontos
* Cruzou entre 61km a 75Km, levou multa de 3 pontos
* Cruzou acima de 75Km, levou multa de 7 pontos
'''
velocidade = 40
if velocidade <= 50:
    print("Não foi multado")
elif velocidade >= 51 and velocidade <= 60:
    print("Levou multa de 2 pontos")
elif velocidade >= 61 and velocidade <= 75:
    print("Levou multa de 3 pontos")
else:
    print("Levou multa de 7 pontos")

# comparação com Chaining
if velocidade <= 50:
    print("Não foi multado")
elif 51 <= velocidade <= 60:
    print("Levou multa de 2 pontos")
elif 61 >= velocidade <= 75:
    print("Levou multa de 3 pontos")
else:
    print("Levou multa de 7 pontos")

# Desafio
# Monte o seguinte cenário usando condicionais
# Você está montando um sistema para um salão de beleza para calcular o preço do corte de cabelos grandes que irá seguir as seguinte regras
'''
Se seu cabelo estiver com ou abaixo de 20cm você paga o valor de R$50,00
Se seu cabelo estiver entre 21cm a 30cm você paga o valor de R$70,00
Se seu cabelo estiver entre 31cm a 50cm você paga o valor de R$100,00
Acima de 50cm Favor consultar na recepção
Declare uma variável que represente o tamanho atual do cabelo
Apenas imprima na tela a mensagem apropriada, nada além disso é necesário
'''
tamanho_cabelo = 51
if tamanho_cabelo <= 20:
    print("Valor do corte R$50,00")
elif 21 <= tamanho_cabelo <= 30:
    print("Valor do corte R$70,00")
elif 31 <= tamanho_cabelo <= 50:
    print("Valor do corte R$100,00")
else:
    print("Favor consultar na recepção")
