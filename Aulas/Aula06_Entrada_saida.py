#Funções de entrada e saída 
#input : Ler dados de entrada do teclado 
#Entrada : print , saída : Input 
nome=input("Qual o seu nome:  ")
idade=input("Quantos anos voce tem: ")
print(f'O seu nome é {nome}')
print(f'A sua idade é de {idade} anos')
#Valores com a função print 
nome="Luiz"
Sobrenome="Medeiros"
print(nome,Sobrenome)
print(nome,Sobrenome, end ="...\n")#Ao final com "end e \n" vai printar com "..." no final
print(nome,Sobrenome, sep="-")#Um separador "-" ,entre nome e sobrenome
