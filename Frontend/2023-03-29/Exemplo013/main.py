turma = input("Digite a turma:")
for cont in range(5):
    matricula = input("Digite a matricula:")
    nome = input("Digite o nome:")
    teste = float(input("Digite a nota do teste: "))
    prova = float(input("Digite a nota da prova: "))
    media = (teste + prova)/2
    if media>=7:
        status = "Aprovado"
    else:
        status = "Reprovado"
    print("Turma: ", turma)
    print("Matricula: ", matricula)
    print("Nome: ", nome)
    print("Média: ", media)
    print("Situação: ", status)