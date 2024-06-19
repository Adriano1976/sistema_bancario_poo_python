"""
Módulo principal do sistema bancário.

Este módulo fornece a função `main` que é responsável por controlar o fluxo principal do programa.
O programa permite a criação de clientes e contas bancárias, além de operações como depósito,
saque e exibição de extratos.

Importa as funções necessárias do módulo `menu`:
- `menu`
- `depositar`
- `sacar`
- `exibir_extrato`
- `criar_cliente`
- `criar_conta`
- `listar_contas`
"""

from menu import (
    menu,
    depositar,
    sacar,
    exibir_extrato,
    criar_cliente,
    criar_conta,
    listar_contas
)


def main():
    """
    Função principal que controla o fluxo do programa.

    Esta função inicializa listas de clientes e contas, e entra em um loop infinito onde exibe
    um menu e executa ações baseadas na opção escolhida pelo usuário. As opções incluem:
    - 'd': Depositar dinheiro em uma conta.
    - 's': Sacar dinheiro de uma conta.
    - 'e': Exibir extrato de uma conta.
    - 'nu': Criar um novo cliente.
    - 'nc': Criar uma nova conta.
    - 'lc': Listar todas as contas.
    - 'q': Sair do programa.

    A função valida a entrada do usuário e exibe uma mensagem de erro para entradas inválidas.
    """
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)
        elif opcao == "s":
            sacar(clientes)
        elif opcao == "e":
            exibir_extrato(clientes)
        elif opcao == "nu":
            criar_cliente(clientes)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            break
        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")


if __name__ == "__main__":
    main()
