# IMC
n = ("bernardo")
p = 60 
h = 1.70 
imcc = p / (h * h)

print("Esses sao seus dados")
print("Meu nome é", n)
print("Tenho o peso de", p, ("kg;"))
print("Minha altura é", h, ("cm;"))
print("Esse é seu IMC", imcc)

###############################

nome = 'Luiz Otávio'
altura = 1.80
peso = 95
imc = peso / altura ** 2

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Luiz Otávio tem 1.80 de altura,
# pesa 95 quilos e seu IMC é
# 29.320987654320987