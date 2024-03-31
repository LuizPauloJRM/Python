#Operadores lógicos 
#And(e) : Os dois devem ser verdadeiros para que retorne verdadeiro "True"
#or(ou) : Ou um ou outra considirem retorna verdadeiro , pelo menos uma condição verdadeira "True"
#not(falso) : Inverte  
saldo = 1000
saque = 250 
limite = 200
conta_especial =True
print(True and True)
print(True and True and True)
print(True and True and False)
print(True and False)
print(True or True)
print(True or False)
print(False or False)


exp_01=saldo >= saque and saque <= limite or conta_especial and saldo >= saque 
print(exp_01)

exp_02=(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_02)
#Verificar se o saldo e suficiente 
conta_normal_com_saldo = (saldo>= saque and saque <= limite)
conta_especial_com_saldo =(conta_especial and saldo >= saque)
exp_03=conta_normal_com_saldo or conta_especial_com_saldo
print (exp_03)
