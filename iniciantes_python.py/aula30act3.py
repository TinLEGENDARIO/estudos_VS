# tamanhos de nome:
print("Escreva o seu nome")
nome = input()
normal = len(nome) >= 4 and len(nome) <6
try:
    if len(nome) <4:
        print("Nome pequeno")
    elif normal:
        print("Nome normal")
    elif len(nome) >= 6:
        print("Nome grande")
except:
    print("Isso não é um nome")
