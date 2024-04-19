#Estruturas de repetição 
#Repetir ate que um trecho de código alcance o objetivo desejado 
#a = int(input("Digite um número : "))
#print (a)
#repita 2 vezes:
# a = +1 
# print (a)
# For função build-in range
#Comando for -> Percorrer um objeto iteravel, quando sabemos o número exato de vezes 
# for letra in texto
#texto= input("Informe um texto: ")
#VOGAIS="AEIOU"
#for letra in texto:
#if letra.upper() in VOGAIS:
# print(letra, end="")
#print () -> Quebra de linha  
# While ->
texto= input("Informe um texto: ")
VOGAIS="AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()
    print ("Executa fim do laço")