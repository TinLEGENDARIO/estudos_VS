#projeto teste
print("Digite um número inteiro:")
a = int(input())
print("Digite outro número inteiro:")
b = int(input())
if a > b:
    print("O primeiro número é maior que o segundo.")
elif a < b:
    print("O segundo número é menor que o primeiro.")
print("esse foi o resultado da comparação")
# This is a simple program that compares two numbers and prints the result.    

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor >= segundo_valor:
    print(
        f'{primeiro_valor=} é maior ou igual '
        f'ao que {segundo_valor=}'
    )
else:
    print(
        f'{segundo_valor=} é maior '
        f'do que {primeiro_valor=}'
    )