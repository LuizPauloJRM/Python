#Conta Bancária 
#conta=5000
#deposito=input("Digite um valor para depositar em sua conta : ")

class ContaBancaria:#Definição de classe #ContaBancaria
    def __init__(self, saldo_inicial):#Inicialização da Classe ContaBancaria: ,cria o "__init__" automaticamente após a criação de uma classe 
        self.saldo = saldo_inicial#Inicializa o atributo saldo do objeto com o valor fornecido saldo_inicial.

    def depositar(self, valor):#Método depositar 
        self.saldo += valor#Define um método chamado depositar que permite depositar um valor na conta.
        print("Depósito de", valor, "realizado com sucesso.")
        print("Saldo atual:", self.saldo)#Saldo atual do depósito


def main():#Função main , função principal do programa
    saldo_inicial = 5000
    conta = ContaBancaria(saldo_inicial)# Cria um objeto conta da classe ContaBancaria com o saldo inicial especificado.

    while True:#Cria um loop infinito.
        try:#Inicia um bloco de código que pode lançar exceções.
            valor_deposito = float(input("Digite o valor do depósito (ou 0 para sair): "))#solicita ao usuário que insira o valor do depósito como um número real
            if valor_deposito == 0:#Verifica se o usuário deseja sair do programa, se o valor do depósito for zero para nao para a execução do programa.
                print("Encerrando o programa.")
                break#Encerra o loop
            elif valor_deposito < 0:#Verifica se o valor do depósito é negativo
                print("Valor de depósito inválido. Por favor, digite um valor positivo.")#Exibe uma mensagem de erro se o valor do depósito for negativo
            else:#Executa se o valor do depósito for válido
                conta.depositar(valor_deposito)
        except ValueError:# Captura a exceção se o valor inserido não puder ser convertido para um número real.
            print("Por favor, digite um valor numérico válido.")# Exibe uma mensagem de erro se o valor inserido não for numérico.


if __name__ == "__main__":#verifica se o script está sendo executado diretamente
    main()#chama a função main para iniciar a execução do programa.