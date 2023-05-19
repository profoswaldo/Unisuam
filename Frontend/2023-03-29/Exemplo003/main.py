lado1 = int(input("Digite o valor do lado 1: "))
lado2 = int(input("Digite o valor do lado 2: "))
lado3 = int(input("Digite o valor do lado 3: "))

if (lado1+lado2)<=lado3:
    print("Não é triangulo")
elif (lado2 + lado3) <=lado1:
    print("Não é triangulo")
elif (lado3 + lado1) <= lado2:
    print("Não é triangulo")
else:
    print("É triangulo")

