class SistemaBancario:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')

    def sacar(self, valor):
        if self.saldo >= valor and valor <= 500 and len(self.saques) < 3:
            self.saldo -= valor
            self.saques.append(valor)
            print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
        elif valor > 500:
            print('Limite máximo de saque por operação é de R$ 500.00.')
        elif len(self.saques) >= 3:
            print('Limite de 3 saques diários atingido.')
        else:
            print('Saldo insuficiente para saque.')

    def extrato(self):
        print('\nExtrato:')
        if not self.depositos and not self.saques:
            print('Não foram realizadas movimentações.')
        else:
            for deposito in self.depositos:
                print(f'Depósito: R$ {deposito:.2f}')
            for saque in self.saques:
                print(f'Saque: R$ {saque:.2f}')
            print(f'Saldo atual: R$ {self.saldo:.2f}')

def main():
    sistema = SistemaBancario()

    while True:
        print("\nEscolha uma opção:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Sair")

        escolha = int(input())

        if escolha == 1:
            valor = float(input("Digite o valor do depósito: "))
            sistema.depositar(valor)
        elif escolha == 2:
            valor = float(input("Digite o valor do saque: "))
            sistema.sacar(valor)
        elif escolha == 3:
            sistema.extrato()
        elif escolha == 4:
            break
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
