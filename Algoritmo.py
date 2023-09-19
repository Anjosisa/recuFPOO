from Classes import *
import os

os.system("cls")

def Main ():
    banco = Banco()

    while True:
        try:
            print("Bem vido! Você está no seu sistema bancário. O que deseja realizar?")
            print("")
            print("1 - Criar conta")
            print("2 - Sacar")
            print("3 - Depositar")
            print("4 - Transferir")
            print("5 - Saldo")
            print("")

            menu = int(input(">>> "))

            match menu:
                case 1:
                    print("Você optou por criar uma conta. Por favor, preencha as instruções abaixo")
                    print(input("Digite o seu nome > "))
                    print("")
                    print(input("Digite seu saldo inicial > "))
                    os.system("pause")
                    os.system("cls")

                case 2:
                    print("Deseja sacar um valor da sua conta?")
                    print("")
                    print (input("Digite o valor que deseja retirar > "))
                    os.system("pause")
                    os.system("cls")

                case 3:
                    print("Sua opção é para fazer um depósito\nQual a quantia que deseja depositar na sua conta?")
                    print (input(">>>"))
                    os.system("pause")
                    os.system("cls")
                    

                case 4:
                    print (input("Na área de transferência, alguns passos precisam ser realizados.\nInforme a conta de origem >\n Digite o destinatário para qual deseja enviar >\n "))
                
                case 5:
                    print("Você entrou em saldo")
                    print("Verifique o saldo atual da sua conta")


        except Exception as erro:
            print("Valor invalido")
            print(erro.__class__.__name__)