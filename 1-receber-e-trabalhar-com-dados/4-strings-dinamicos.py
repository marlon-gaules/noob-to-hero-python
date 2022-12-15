# Exemplo abaixo de strings dinâmicos "mensagem personalizada";
#   Quando faço cadastro em um site, e depois ele retorna (Olá Marlon, seja bem vindo!)

# Após me cadastrar abaixo, e retornar para o usuário que deu tudo certo
# O f "formatado" serve para criar strings dinâmicos
nome = "Marlon Costa e Sousa"
email = "marlon.codar@gmail.com"
print(f"Olá {nome}, seu cadastro com {email} foi realizado com sucesso!")

# Monte as palavras "bateria eletrônica" usando as sílabas como base
b = "ba"
parte2 = "nica"
a = "a"
r = "ri"
parte1 = "eletrô"
t = "te"
print(f"{b}{t}{r}{a} {parte1}{parte2}")
