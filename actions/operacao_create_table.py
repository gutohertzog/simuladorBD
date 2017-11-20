"""
    Módulo responsável por realizar as operações de validação e craição com o CREATE TABLE.

    Sintaxe para criação da table:

    CREATE TABLE nome_tabela (
        nome_coluna1 tipo_dados
        nome_coluna2 tipo_dados
        nome_coluna3 tipo_dados
        ....
    );
"""

# import syntax as s

def valida_create_table(lista_query, tipo):
    """
        Função que verifica se a query para criação da table está conforme a sintaxe.

        Para ser válida precisa retornar True.
    """
    # verificação fora dos parênteses
    if verifica_tamanho(lista_query):
        print("Query de tamanho incorreto.")
        return False
    if verifica_digito(lista_query[2]):
        print("O nome da tabela não pode conter apenas números.")
        return False
    if not verifica_parenteses(lista_query[3], lista_query[len(lista_query)-1]):
        print("Parênteses incorreto.")
        return False

    # verificação interna dos parênteses
    atributos = pega_conteudo_parenteses(lista_query)
    if verifica_parametros(atributos, tipo):
        return False

    return True


def verifica_tamanho(lista_query):
    """
        Verifica o tamanho da query.
        Para ter um tamanho válido, precisa retornar False.

        O tamanho mínimo dela é de 7 itens, de acordo com a estrutura abaixo:
        ['create', 'table', 'nome_tabela', '(', 'nome_coluna1', 'tipo_dados', ')']
    """
    return len(lista_query) < 7


def verifica_digito(nome):
    """
        Verifica se o nome da tabela não é composto apenas por dígitos.
        Para ser um nome válido, precisa retornar False.

        False: abc, ab2, 2ab
        True: 123, 12.3
    """
    return nome.isdigit()


def verifica_parenteses(abre, fecha):
    """
        Verifica se os parênteses foram entrados conforme o esperado.
        Para ser válido, precisa retornar True.
    """
    return abre == '(' and fecha == ')'


def pega_conteudo_parenteses(lista_query):
    """
        Separa da query todos os nomes e tipos dos campos da tabela, que ficam entre
        os parênteses.
        Devido a forma de criação da tabela, os itens tem um local fixo para começar e terminar.
    """
    atributos = []
    for item in lista_query[4:-1]:
        atributos.append(item)
    return atributos


def pega_nomes(lista_query):
    """
        Separa os nomes das colunas.
    """
    resultado = []
    colunas = pega_conteudo_parenteses(lista_query)
    for indice, item in enumerate(colunas):
        if indice % 2 == 0:
            resultado.append(item)
    return resultado


def pega_tipos(lista_query):
    """
        Separa os tipos das colunas.
    """
    resultado = []
    colunas = pega_conteudo_parenteses(lista_query)
    for indice, item in enumerate(colunas):
        if indice % 2 == 1:
            resultado.append(item)
    return resultado


def verifica_parametros(atributos, tipo):
    """
        Os atributos precisam ser em pares: nome_coluna1 tipo_dados, nome_coluna2 tipo_dados...

        Para ser válido, precisa retornar False.
    """
    # já que serão sempre pares, o resto da divisão por 2 tem que ser 0.
    if len(atributos) % 2 == 0:
        index_nome = 0
        lista_nome = []
        index_tipo = 1
        lista_tipo = []
        # passa para as listas diferentes os nomes e tipos
        for indice, item in enumerate(atributos):
            if verifica_digito(item):
                print("O nome da coluna não pode ser apenas dígitos.")
                return True
            if indice % 2 == index_nome:
                lista_nome.append(item)
            elif indice % 2 == index_tipo:
                lista_tipo.append(item.upper())
        # verifica se os tipos estão dentro dos tipos possíveis
        if set(tipo).issubset(lista_tipo) or set(tipo).issuperset(lista_tipo):
            return False
        else:
            print("Os tipos das colunas estão incorretos.")
    return True


def verifica_nome(nome, tabelas):
    """
        Verifica se o nome da nova tabela já não está sendo usado.

        Para ser válido, precisa retornar True.
    """
    for item in tabelas:
        if item['nome_tabela'] == nome:
            print("Nome de tabela já utilizado.")
            return False
    return True


def cria_tabela(lista_query):
    """
        Cria a nova tabela.

        Modelo da nova tabela:
        {
            "nome_tabela": "teste",
            "coluna_tipo": ["int", "varchar"],
            "coluna_nome": ["id", "nome"],
            "dados": [
                [1, "guto"],
                [2, "cara"],
                [3, "alguém"],
                ...
            ]
        }
    """
    nova_tabela = {}
    tipos = pega_tipos(lista_query)
    nomes = pega_nomes(lista_query)
    nova_tabela['nome_tabela'] = lista_query[2]
    nova_tabela['coluna_tipo'] = tipos
    nova_tabela['coluna_nome'] = nomes
    nova_tabela['dados'] = []
    print("Tabela criada com sucesso.")

    return nova_tabela
