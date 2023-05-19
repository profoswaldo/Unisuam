matricula = input("Digite a matricula do Funcionario: ")
nome = input("Digite o nome do Funcionario: ")
salarioBase = float(input("Digite o valor do salário Base: "))
numeroDependentes = int(input("Digite o numero de Dependentes: "))
vendas = float(input("Digite o valor das Vendas: "))

salarioFamilia = (salarioBase*1/100) * numeroDependentes

comissaoVendas = 0
if vendas > 3000:
    comissaoVendas = 200



salarioBruto = salarioBase + salarioFamilia + comissaoVendas

inss = salarioBruto * 11/100

if salarioBruto<1400:
    ir = 0
elif salarioBruto>= 5000:
    ir = salarioBruto * 27.5/100
elif salarioBruto>=3000:
    ir = salarioBruto * 20 / 100
else:
    ir = salarioBruto * 15 / 100

salarioLiquido = salarioBruto - inss - ir

print(matricula)
print(nome)
print(salarioLiquido)


