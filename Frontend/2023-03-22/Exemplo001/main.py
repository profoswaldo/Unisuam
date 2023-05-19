numero1 = float(input("Digite o primeiro valor: ")) 
numero2 = float(input("Digite o segundo valor: "))

if numero1 == numero2:
   mensagem = "numero1 e numero2 são iguais"
else:
   if numero1>numero2:
     mensagem = "Numero 1 é Maior"
   else:
     mensagem = "Numero 2 é Maior"

print(mensagem)