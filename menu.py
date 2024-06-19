"""
Módulo para gerenciar transações bancárias, contas e clientes.

Este módulo contém funções para realizar operações bancárias como depósito,
saque, exibição de extrato, criação de cliente e conta, e listagem de contas.
"""


import textwrap
from transacao import Deposito, Saque
from cliente import PessoaFisica
from conta import ContaCorrente
from validador_cpf import ValidadorCPF
from datetime import datetime


def menu():
    """
    Exibe o menu principal e retorna a opção escolhida pelo usuário.

    Returns:
        str: A opção escolhida pelo usuário.
    """
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def filtrar_cliente(cpf, clientes):
    """
    Filtra e retorna o cliente com o CPF informado.

    Args:
        cpf (str): O CPF do cliente a ser filtrado.
        clientes (list): A lista de clientes cadastrados.

    Returns:
        PessoaFisica: O cliente correspondente ao CPF informado, ou None se não encontrado.
    """
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    """
    Recupera a primeira conta associada ao cliente.

    Args:
        cliente (PessoaFisica): O cliente cuja conta será recuperada.

    Returns:
        ContaCorrente: A primeira conta do cliente, ou None se o cliente não possuir conta.
    """
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return
    return cliente.contas[0]


def depositar(clientes):
    """
    Realiza uma operação de depósito para um cliente.

    Args:
        clientes (list): A lista de clientes cadastrados.
    """
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
    """
    Realiza uma operação de saque para um cliente.

    Args:
        clientes (list): A lista de clientes cadastrados.
    """
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes):
    """
    Exibe o extrato da conta de um cliente.

    Args:
        clientes (list): A lista de clientes cadastrados.
    """
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    print(f"Titular: {cliente.nome}")
    print(f"Data: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")

    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")


def criar_cliente(clientes):
    """
    Cria um novo cliente.

    Args:
        clientes (list): A lista de clientes cadastrados.
    """
    cpf = input("Informe o CPF (somente número): ")
    if not ValidadorCPF.validar(cpf):
        print("\n@@@ CPF inválido! @@@")
        return
    cliente = filtrar_cliente(cpf, clientes)
    if cliente:
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(cliente)
    print("\n=== Cliente criado com sucesso! ===")


def criar_conta(numero_conta, clientes, contas):
    """
    Cria uma nova conta para um cliente existente.

    Args:
        numero_conta (str): O número da nova conta.
        clientes (list): A lista de clientes cadastrados.
        contas (list): A lista de contas cadastradas.
    """
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
        return
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)
    print("\n=== Conta criada com sucesso! ===")


def listar_contas(contas):
    """
    Lista todas as contas cadastradas.

    Args:
        contas (list): A lista de contas cadastradas.
    """
    for conta in contas:
        print("=" * 40)
        print(textwrap.dedent(str(conta)))
