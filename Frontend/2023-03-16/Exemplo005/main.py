nome = input("Digite o nome: ")
salario_bruto = float(input("Digite o salário bruto: "))
numero_dependentes = int(input("Digite o número de dependentes: "))


salario_familia = 80 * numero_dependentes

inss = salario_bruto*11/100

if salario_bruto >= 2000:
  ir = salario_bruto * 20 /100
else:
  ir = 0

salario_liquido = salario_bruto + salario_familia - inss - ir

print(nome, salario_liquido)