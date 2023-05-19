nome = input("Digite o nome: ")
salbruto = float(input("Digite o seu salario bruto: "))
ndep = int(input("Digite o numero de dependentes:")) 
inss = salbruto * 11/100
salfam = 100 * ndep
saliq = salbruto + salfam - inss
print(nome,saliq)




