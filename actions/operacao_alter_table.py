"""
    Módulo responsável por realizar as operações de alteração com o ALTER TABLE.

    Sintaxe para as alterações da table:

    -- adiciona uma nova coluna
    ALTER TABLE nome_tabela ADD nome_coluna tipo_dados;

    -- deleta uma coluna existente apenas se a tabela for vazia
    ALTER TABLE nome_tabela DROP COLUMN nome_coluna;

    INCOMPLETO!
"""


def valida_alter_table(lista_query, tabelas):
    """
        Função que verifica se a query para alteração da table está conforme a sintaxe.
    """
    if verifica_tamanho(lista_query):
        print("Query de tamanho incorreto.")
        return False
    if verifica_digito(lista_query[2]):
        print("Nome da tabela inválido.")
        return False
    if verifica_nome_tabelas(lista_query[2], tabelas):
        print("Tabela inexistente.")
        return False
    return True


def valida_add(lista_query, termo_meio, tipo):
    """
        Para ser válido, precisa retornar True.
    """
    # verifica se a query tem ADD e não tem DROP nem COLUMN
    if termo_meio[0].lower() in lista_query and termo_meio[1].lower() not in lista_query and \
       termo_meio[2].lower() not in lista_query:
        if lista_query[5].upper() in tipo:
            return True
    return False


def valida_drop(lista_query, termo_meio):
    """
        Para ser válido, precisa retornar True.
    """
    # verifica se a query tem DROP e COLUMN e não tem ADD
    if termo_meio[1].lower() in lista_query and termo_meio[2].lower() in lista_query and \
       termo_meio[0].lower() not in lista_query:
        if lista_query[3] == termo_meio[1].lower() and lista_query[4] == termo_meio[2].lower():
            return True
    return False


def adiciona_coluna(lista_query):
	"""
        Para ser válido, precisa retornar True.
    """


def verifica_tamanho(lista_query):
    """
        Verifica o tamanho da query.
        Para ter um tamanho válido, precisa retornar False.

        O tamanho mínimo dela é de 6 itens, de acordo com as estruturas abaixo:
        ['alter', 'table', 'nome_tabela', 'add', 'nome_coluna', 'tipo_dados']
        ['alter', 'table', 'nome_tabela', 'drop', 'column', 'nome_coluna']
    """
    return not len(lista_query) == 6


def verifica_nome_tabelas(nome, tabelas):
    """
        Verifica se o nome referencia uma tabela que já existe.

        Para ter um tamanho válido, precisa retornar False.
    """
    for item in tabelas:
        if item['nome_tabela'] == nome:
            return False
    return True


def verifica_digito(nome):
    """
        Verifica se o nome da tabela não é composto apenas por dígitos.
        Para ser um nome válido, precisa retornar False.

        False: abc, ab2, 2ab
        True: 123, 12.3
    """
    return nome.isdigit()
