class ValidadorCPF:
    """
    Classe para validação de CPF (Cadastro de Pessoas Físicas) brasileiros.

    Esta classe contém um método estático para validar se um CPF fornecido é válido,
    conforme as regras definidas pela Receita Federal do Brasil.

    Methods:
        validar(cpf: str) -> bool
            Valida o número de CPF fornecido.
    """

    @staticmethod
    def validar(cpf):
        """
        Valida um número de CPF.

        Este método remove todos os caracteres não numéricos do CPF fornecido e verifica se ele possui 11 dígitos.
        Em seguida, ele realiza os cálculos dos dígitos verificadores para determinar se o CPF é válido.

        Args:
            cpf (str): O número de CPF a ser validado.

        Returns:
            bool: True se o CPF for válido, False caso contrário.
        """
        cpf = ''.join(filter(str.isdigit, cpf))
        if len(cpf) != 11 or cpf == cpf[0] * len(cpf):
            return False

        for i in range(9, 11):
            soma = sum(int(cpf[num]) * ((i + 1) - num) for num in range(0, i))
            digito = ((soma * 10) % 11) % 10
            if digito != int(cpf[i]):
                return False

        return True
