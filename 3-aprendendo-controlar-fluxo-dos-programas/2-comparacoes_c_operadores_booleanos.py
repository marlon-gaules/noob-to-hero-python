# temos duas informações da pessoa, a idade e o convite.
# então a condição, é que a pessoa só pode entrar no evento caso seja maior de 21 anos, e tenha um convite
idade = 21
possui_convite = False
filho_do_dono = True

# uma condição, envolvendo duas condicionais (and), atende se as duas condições estiver de acordo
print(idade >= 21 and possui_convite == True)

# o (or) atende se alguma condição estiver de acordo
print(idade >= 21 or possui_convite == True)

# envolvendo 3 condições
# informo que aceito alguma das duas opções abaixo
print((idade >= 21 and possui_convite == True) or (filho_do_dono == True))

# você só pode trabalhar aqui se for maior idade e possuir carteira de trabalho
maior_idade = True
possui_carteira_de_trabalho = False
possui_veiculo_proprio = True

print(maior_idade == True and possui_carteira_de_trabalho == True)
# posso imprimir o mesmo resultado acima, diminuindo a linha de código
print(maior_idade and possui_carteira_de_trabalho)

# negativando uma condição
# queremos contratar pessoas que ainda não possuem veiculo próprio, mas já possuam uma carteira de trabalho
print(possui_carteira_de_trabalho == True and not possui_veiculo_proprio)

# Desafio

'''Defina as seguintes variáveis, inicialmente todas como False, a ideia aqui não é se importar com os valores dentro dessas variáveis, mas sim como montar condicionais.

possui_passaporte = False
passagem_comprada = False
menor_Idade = False

Crie as seguintes condições e imprima o resultado na tela.
Uma pessoa só pode viajar se possuir passaporte e tiver a passagem comprada e não for menor idade
Uma pessoa só pode viajar se possuir passaporte ou tiver a passagem comprada e não for menor idade
Uma pessoa só pode viajar se não possuir passaporte ou tiver a passagem comprada e não for menor idade
Uma pessoa não pode viajar se não possuir passaporte ou não tiver a passagem comprada e for menor idade'''
possui_passaporte = False
passagem_comprada = False
menor_Idade = False

print((possui_passaporte and passagem_comprada) and not menor_Idade)
print((possui_passaporte or passagem_comprada) and not menor_Idade)
print((not possui_passaporte or passagem_comprada) and not menor_Idade)
print((not possui_passaporte or not passagem_comprada) and menor_Idade)
