"""
    Módulo responsável por realizar as operações de validação e exclusão com o DROP  TABLE.

    Sintaxe para criação da table:

    DROP TABLE nome_tabela;
"""


def valida_drop_table(lista_query):
    """
        Função que verifica se a query para deleção da table está conforme a sintaxe.

        Para ser válida precisa retornar True.
    """
    if verifica_tamanho(lista_query):
        print("Query de tamanho incorreto.")
        return False
    if verifica_digito(lista_query[2]):
        print("O nome da tabela não pode conter apenas números.")
        return False
    return True


def verifica_tamanho(lista_query):
    """
        Verifica o tamanho da query.
        Para ter um tamanho válido, precisa retornar False.

        O tamanho fixo dela é de 3 itens, de acordo com a estrutura abaixo:
        ['drop', 'table', 'nome_tabela']
    """
    return len(lista_query) != 3


def verifica_digito(nome):
    """
        Verifica se o nome da tabela não é composto apenas por dígitos.
        Para ser um nome válido, precisa retornar False.

        False: abc, ab2, 2ab
        True: 123, 12.3
    """
    return nome.isdigit()


def verifica_nome(nome, tabelas):
    """
        Verifica se o nome da nova tabela já não está sendo usado.

        Para ser válido, precisa retornar True.
    """
    for item in tabelas:
        if item['nome_tabela'] == nome:
            return True
    print("Tabela não existente.")
    return False


def deleta_tabela(nome, tabelas):
    """
        Retorna o índice da tabela a ser deletada da lista.
    """
    for indice, item in enumerate(tabelas):
        if item['nome_tabela'] == nome:
            return indice
