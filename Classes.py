import random

class Cliente:
    def __init__(self, nome, saldoi):
        nome = nome 
        saldoi = saldoi

class Banco:
    def __init__(self):
        self.clientes = {}

    def criar_conta(self, nome, id):
        id = random.randint(1000, 10000)
        self.clientes[id] = self.clientes
        print (f"{nome} adicionado, o id é {id}")

    def Sacar(self, id, x):
        s = 0
        for conta, valor in self.clientes.items():
            if conta == id:
                s = 1
                if valor.saldoi >= 0 and x <= valor.saldoi:    
                    valor.saldoi = valor.saldoi - x
                    print(f"O Valor do saldo atual é de: R${valor.saldoi}, você sacou {x}")
                    break
                else:
                    print("Saldo insuficiente")                
        if s != 1:
            print("Cliente não encontrado")

    def Depositar (self, x):
        d = 0
        for chave, valor in self.clientes.items():
            if chave == id:
                d = 1
                valor.saldoi = valor.saldoi + x
                print(f"O Valor do saldo atual é de: R${valor.saldoi}")
                break
        if d != 1:
            print("Cliente não encontrado")


    def Transferir (self, origem, destino, valor):
        origem = origem
        destino = destino
        valor = valor


    def Saldo (self, valor):
        valor = valor 
