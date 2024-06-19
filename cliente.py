class Cliente:
    """
    Representa um cliente de um banco, que possui um endereço e uma lista de contas.

    Atributos:
        endereco (str): O endereço do cliente.
        contas (list): Lista de contas associadas ao cliente.

    Métodos:
        __init__(self, endereco):
            Inicializa um novo cliente com um endereço fornecido.

        realizar_transacao(self, conta, transacao):
            Realiza uma transação em uma conta específica.

        adicionar_conta(self, conta):
            Adiciona uma nova conta à lista de contas do cliente.
    """

    def __init__(self, endereco):
        """
        Inicializa um novo cliente com um endereço fornecido.

        Parâmetros:
            endereco (str): O endereço do cliente.
        """
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        """
        Realiza uma transação em uma conta específica.

        Parâmetros:
            conta (Conta): A conta onde a transação será realizada.
            transacao (Transacao): A transação a ser realizada.
        """
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        """
        Adiciona uma nova conta à lista de contas do cliente.

        Parâmetros:
            conta (Conta): A conta a ser adicionada.
        """
        self.contas.append(conta)


class PessoaFisica(Cliente):
    """
    Representa um cliente pessoa física, que herda da classe Cliente.

    Atributos:
        nome (str): O nome da pessoa física.
        data_nascimento (str): A data de nascimento da pessoa física.
        cpf (str): O CPF da pessoa física.
        endereco (str): O endereço da pessoa física.

    Métodos:
        __init__(self, nome, data_nascimento, cpf, endereco):
            Inicializa uma nova pessoa física com nome, data de nascimento, CPF e endereço fornecidos.
    """

    def __init__(self, nome, data_nascimento, cpf, endereco):
        """
        Inicializa uma nova pessoa física com nome, data de nascimento, CPF e endereço fornecidos.

        Parâmetros:
            nome (str): O nome da pessoa física.
            data_nascimento (str): A data de nascimento da pessoa física.
            cpf (str): O CPF da pessoa física.
            endereco (str): O endereço da pessoa física.
        """
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
