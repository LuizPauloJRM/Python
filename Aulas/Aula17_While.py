#While 
#Até que algo aconteça 
#Repetição bloco varias vezes 
#Não tem certeza de quantas vezes vai executar 
#Executa toda vez que for atendida
opcao = -1
while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[3] Sair \n: "))
    if opcao == 1:
        print("Saque")
    elif opcao == 2:
        print("Extrato")
