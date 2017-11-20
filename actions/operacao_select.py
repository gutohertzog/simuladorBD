"""
    Módulo responsável por realizar as operações de validação e execução com o SELECT.

    Sintaxe para consulta dos dados.
    SELECT coluna1, coluna2, ...
        FROM nome_tabela;
    ou
    SELECT *
        FROM nome_tabela;
"""


def valida_select(lista_query, termo_meio, tabelas):
    """
        pass
    """
    v_from = 0
    # verifica se o termo FROM está presente na query
    if termo_meio.lower() not in lista_query:
        print("Faltou o termo FROM.")
        return False
    # armazena o índice do FROM
    v_from = lista_query.index(termo_meio.lower())
    # pega o nome da tabela
    nome_tabela = lista_query[v_from + 1]

    if verifica_digito(nome_tabela):
        return False
    if valida_nomes(lista_query[-1], tabelas):
        return False
    return True


def valida_nomes(nome, tabelas):
    """
        Verifica se o nome das tabela está correto.

        Para ser válido, precisa retornar False.
    """
    for item in tabelas:
        if item['nome_tabela'] == nome:
            return False
    print("Tabela inexistente.")
    return True


def verifica_digito(nome):
    """
        Verifica se o nome da tabela não é composto apenas por dígitos.
        Para ser um nome válido, precisa retornar False.

        False: abc, ab2, 2ab
        True: 123, 12.3
    """
    return nome.isdigit()


def retorna_valores(lista_query, tabelas):
    """
        pass
    """
    for item in tabelas:
        if item['nome_tabela'] == lista_query[-1]:
            print(item['dados'])
