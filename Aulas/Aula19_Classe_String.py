#Strings
#Conversão de strings (upper,lower,title )
#curso=python
#print(curso.upper()) PYTHON print(curso.lower()) python print(curso.title()) Python...
#Maiusculo , minusculo , título 
#Espacos em branco: Strip, lstrip , rstrip  print(curso.strip())
#Centralização e junções : center, join print(curso.center(10,"#")) ##Python## ,mais 4 caracteres para completar 10
#print('.'.join(curso)) P.y.t.h.o.n , cada passe coloca um "." , letra por letra "junção"
nome = "LuIz"
print(nome.upper())
print(nome.lower())
print(nome.title())
#Eliminar espaços em branco 
print("Eliminar espaços em branco")
nome = "  Luiz  "
print(nome)
print(nome.strip())
print(nome.rstrip())
print(nome.lstrip()+".")
print("Junção e centralização")
nome = "Luiz"
print("#####" + nome + "#####")
print(nome.center(14))
print(nome.center(20),"#")
print("Juntando")
menu = "Python"
print("-".join(menu))

