mat = input("Digite a matricula: ")
nome = input("Digite o nome: ")
n1 = float(input("Digite N1: "))
n2 = float(input("Digite N2: "))
n3 = float(input("Digite N3: "))

media = (n1+ n2+n3)/3

if media < 7:
  situacao = "Reprovado"
else:
  situacao = "Aprovado"

print("Matricula: ", mat)
print("Nome: ", nome)
print("Média: ", media)
print("Situação: " ,situacao)