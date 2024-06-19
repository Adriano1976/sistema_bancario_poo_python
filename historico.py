"""
Módulo que define a classe Historico para gerenciar transações financeiras.
"""

from datetime import datetime


class Historico:
    """
    Classe que representa o histórico de transações financeiras.

    Métodos:
        __init__() - Inicializa uma nova instância da classe Historico.
        transacoes() - Retorna a lista de transações.
        adicionar_transacao(transacao) - Adiciona uma nova transação ao histórico.
    """

    def __init__(self):
        """
        Inicializa uma nova instância da classe Historico.
        """
        self._transacoes = []

    @property
    def transacoes(self):
        """
        Retorna a lista de transações.

        Retorna:
            list: Lista de dicionários, onde cada dicionário representa uma transação.
        """
        return self._transacoes

    def adicionar_transacao(self, transacao):
        """
        Adiciona uma nova transação ao histórico.

        Parâmetros:
            transacao (objeto): O objeto de transação a ser adicionado. Espera-se que o objeto tenha
            um atributo `valor`.
        """
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )
