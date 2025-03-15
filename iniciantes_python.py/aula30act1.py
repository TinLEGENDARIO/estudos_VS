print("Escreva um numero inteiro:")
numero = input()
try:
    numero_int = int(numero)
    print(f"O número que você digitou é {numero_int}")
    if numero_int % 2 == 0:
        print("O número é par")
    else:
        print("O número é ímpar")
except:
    print("Isso não é um número inteiro")

