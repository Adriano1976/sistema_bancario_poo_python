"""
Módulo para gerenciamento de contas bancárias, incluindo contas correntes com limites e histórico de transações.

Classes:
    Conta: Representa uma conta bancária básica.
    ContaCorrente: Representa uma conta corrente com limites de saque e número máximo de saques.
"""

from historico import Historico


class Conta:
    """
    Classe que representa uma conta bancária.

    Atributos:
        _saldo (float): Saldo da conta.
        _numero (str): Número da conta.
        _agencia (str): Agência da conta.
        _cliente (object): Cliente associado à conta.
        _historico (Historico): Histórico de transações da conta.

    Métodos:
        __init__(self, numero, cliente): Inicializa uma nova instância de Conta.
        nova_conta(cls, cliente, numero): Cria uma nova conta para um cliente.
        saldo(self): Retorna o saldo da conta.
        numero(self): Retorna o número da conta.
        agencia(self): Retorna a agência da conta.
        cliente(self): Retorna o cliente associado à conta.
        historico(self): Retorna o histórico de transações da conta.
        sacar(self, valor): Realiza um saque na conta.
        depositar(self, valor): Realiza um depósito na conta.
    """

    def __init__(self, numero, cliente):
        """
        Inicializa uma nova instância de Conta.

        Args:
            numero (str): Número da conta.
            cliente (object): Cliente associado à conta.
        """
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        """
        Cria uma nova conta para um cliente.

        Args:
            cliente (object): Cliente que será associado à nova conta.
            numero (str): Número da nova conta.

        Returns:
            Conta: Uma nova instância de Conta.
        """
        return cls(numero, cliente)

    @property
    def saldo(self):
        """Retorna o saldo da conta."""
        return self._saldo

    @property
    def numero(self):
        """Retorna o número da conta."""
        return self._numero

    @property
    def agencia(self):
        """Retorna a agência da conta."""
        return self._agencia

    @property
    def cliente(self):
        """Retorna o cliente associado à conta."""
        return self._cliente

    @property
    def historico(self):
        """Retorna o histórico de transações da conta."""
        return self._historico

    def sacar(self, valor):
        """
        Realiza um saque na conta.

        Args:
            valor (float): Valor a ser sacado.

        Returns:
            bool: True se o saque foi realizado com sucesso, False caso contrário.
        """
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        return False

    def depositar(self, valor):
        """
        Realiza um depósito na conta.

        Args:
            valor (float): Valor a ser depositado.

        Returns:
            bool: True se o depósito foi realizado com sucesso, False caso contrário.
        """
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False
        return True


class ContaCorrente(Conta):
    """
    Classe que representa uma conta corrente com limites de saque e número máximo de saques.

    Atributos:
        _limite (float): Limite de saque da conta.
        _limite_saques (int): Número máximo de saques permitidos por dia.

    Métodos:
        __init__(self, numero, cliente, limite=500, limite_saques=3): Inicializa uma nova instância de ContaCorrente.
        sacar(self, valor): Realiza um saque na conta corrente considerando os limites.
        __str__(self): Retorna uma representação em string da conta corrente.
    """

    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        """
        Inicializa uma nova instância de ContaCorrente.

        Args:
            numero (str): Número da conta.
            cliente (object): Cliente associado à conta.
            limite (float, optional): Limite de saque da conta. Padrão é 500.
            limite_saques (int, optional): Número máximo de saques permitidos por dia. Padrão é 3.
        """
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        """
        Realiza um saque na conta corrente considerando os limites.

        Args:
            valor (float): Valor a ser sacado.

        Returns:
            bool: True se o saque foi realizado com sucesso, False caso contrário.
        """
        from transacao import Saque  # Importação local para evitar importação circular
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )
        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
        else:
            return super().sacar(valor)
        return False

    def __str__(self):
        """
        Retorna uma representação em string da conta corrente.

        Returns:
            str: Representação em string da conta corrente.
        """
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """
