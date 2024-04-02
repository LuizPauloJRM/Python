def verificar_idade(ano_nascimento, ano_atual):
    idade = ano_atual - ano_nascimento
    return idade

ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

idade = verificar_idade(ano_nascimento, ano_atual)
print("A idade é:", idade)