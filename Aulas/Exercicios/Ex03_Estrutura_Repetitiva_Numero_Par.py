#Break
#Exibindo ate que o número seja par 
while True:
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print(numero, "é par")
    else:
        print(numero, "é ímpar")
    continuar = input("Quer continuar? [S/N] ").upper().strip()[0]
    if continuar in "N":
        break
