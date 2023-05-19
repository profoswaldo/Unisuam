
nota1 =float(input("Digite a nota 1: "))
nota2 =float(input("Digite a nota 2: "))

media =(nota1 + nota2)/2

if media>=7:
    status = "Aprovado"
else:
    status = "Reprovado"

print(status)