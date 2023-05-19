import funcoes


nota1 =float(input("Digite a nota 1: "))
nota2 =float(input("Digite a nota 2: "))

media = funcoes.calcular_media(nota1,nota2)

if media>=7:
    status = "Aprovado"
else:
    status = "Reprovado"

print(status)