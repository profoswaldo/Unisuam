altura = float(input("Altura: "))
sexo = input("Sexo M/F")

if sexo == "M":
    peso = (72.7*altura) - 58
else:
    peso = (62.1*altura) - 44.7
print(peso)