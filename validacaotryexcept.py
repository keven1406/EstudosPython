validacao = False
while (validacao != True):
    try:
        x = int(input("Digite um numero inteiro: "))
        validacao = True
        print(f"O valor digitado é {x}")
    except ValueError:
        print("Digite um número válido!")