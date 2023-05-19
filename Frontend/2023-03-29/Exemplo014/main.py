turma = input("Digite a turma:")
matricula = input("Digite a matricula:")
while matricula!="0":
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
    matricula = input("Digite a matricula:")