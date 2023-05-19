# Faça um programa que peça 10 notas, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido


for cont in range(10):
    nota = int(input("Digite a nota: "))
    if nota < 0 or nota >10:
         print("Nota Invalida")



