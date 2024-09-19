opcao = 1
while opcao == 1:
    n = int(input("Digite um numero: "))
    if n % 2 == 0:
        if n > 0:
            print(f"{n} é par e tambem é positivo")
        elif n < 0:
            print(f"{n} é par e tambem é negativo")
    else:
        if n > 0:
            print(f"{n} é impar e tambem é positivo")
        elif n < 0:
            print(f"{n} é impar e tambem é negativo")
    opcao = int(input("Digite 1 para continuar e 2 para finalizar"))
