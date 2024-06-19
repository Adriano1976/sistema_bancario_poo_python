"""
Módulo de transações bancárias.

Este módulo define classes abstratas e concretas para representar transações bancárias,
como saques e depósitos. As transações são registradas em uma conta bancária específica.

Classes:
    Transacao: Classe abstrata base para todas as transações bancárias.
    Saque: Classe para representar uma transação de saque.
    Deposito: Classe para representar uma transação de depósito.

Exceções:
    Nenhuma

Funções:
    Nenhuma

Uso:
    from conta import Conta
    from transacoes import Saque, Deposito

    conta = Conta()
    saque = Saque(100)
    deposito = Deposito(200)

    saque.registrar(conta)
    deposito.registrar(conta)
"""

from abc import ABC, abstractmethod
from conta import Conta


class Transacao(ABC):
    """
    Classe abstrata que define uma transação bancária.

    Propriedades:
        valor (float): Retorna o valor da transação.

    Métodos:
        registrar(conta: Conta): Registra a transação em uma conta.
    """
    @property
    @abstractmethod
    def valor(self):
        """
        Retorna o valor da transação.

        Este método deve ser implementado por subclasses.
        """
        pass

    @abstractmethod
    def registrar(self, conta):
        """
        Registra a transação em uma conta.

        Este método deve ser implementado por subclasses.

        Args:
            conta (Conta): A conta em que a transação será registrada.
        """
        pass


class Saque(Transacao):
    """
    Classe para representar uma transação de saque.

    Args:
        valor (float): O valor do saque.

    Propriedades:
        valor (float): Retorna o valor do saque.

    Métodos:
        registrar(conta: Conta): Registra o saque em uma conta.
    """
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        """
        Retorna o valor do saque.

        Returns:
            float: O valor do saque.
        """
        return self._valor

    def registrar(self, conta: Conta):
        """
        Registra o saque em uma conta.

        Args:
            conta (Conta): A conta em que o saque será registrado.
        """
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    """
    Classe para representar uma transação de depósito.

    Args:
        valor (float): O valor do depósito.

    Propriedades:
        valor (float): Retorna o valor do depósito.

    Métodos:
        registrar(conta: Conta): Registra o depósito em uma conta.
    """
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        """
        Retorna o valor do depósito.

        Returns:
            float: O valor do depósito.
        """
        return self._valor

    def registrar(self, conta: Conta):
        """
        Registra o depósito em uma conta.

        Args:
            conta (Conta): A conta em que o depósito será registrado.
        """
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
