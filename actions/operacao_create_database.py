"""
    Módulo responsável por realizar as operações de validação e execução com o CREATE DATABASE.

    Sintaxe para criação da database:

    CREATE DATABASE nome_base_dados;
"""


def valida_create_database(lista_query):
    """
        Função que valida se a query para criação da database está conforme a sintaxe.
    """
    # número de palavras que a query precisa ter
    if len(lista_query) == 3:
        # verifica se o nome da database não é apenas dígitos
        if not lista_query[2].isdigit():
            # retorna True caso esteja tudo ok
            return True
    # retorna False caso algo esteja errado
    return False


def verifica_nome(nome, nomes_database):
    """
        Verifica se o novo nome da databse já não foi usado em alguma outra.
    """
    # verifica se o nome da nova database já não está sendo usado
    if nome not in nomes_database:
        # nome ainda não usado
        return True
    # nome já usado
    return False
