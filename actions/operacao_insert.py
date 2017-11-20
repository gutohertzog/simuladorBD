"""
    Módulo responsável por realizar as operações de validação e execução com o INSERT.

    Sintaxe para criação da table:
    INSERT INTO nome_tabela VALUES (
        valor1,
        valor2,
        valor3,
        ...
    );
"""


def valida_insert(lista_query, termo_meio):
    """
        pass
    """
    if verifica_digito(lista_query[2]):
        print("O nome da tabela não pode ser dígitos.")
        return False
    if lista_query[3].upper() != termo_meio:
        print("Faltou o termo VALUES.")
        return False
    return True


def valida_nomes(lista_query, tabelas):
    """
        Verifica se o nome das tabela está correto.

        Para ser válido, precisa retornar True.
    """
    nome = lista_query[2]
    for item in tabelas:
        if item['nome_tabela'] == nome:
            atributos = pega_conteudo_parenteses(lista_query)
            if len(item['coluna_nome']) == len(atributos):
                # print(atributos)
                return True
            else:
                print("Campos insuficientes.")
        # else:
        #     print("Tabela inexistente.")
    return False


def insere(lista_query, tabelas):
    """
        Insere os valores dos campos na tabela.

        BUG AINDA ESTÁ INSERINDO DUPLICADO A ID
    """
    # print(lista_query)
    nome = lista_query[2]
    for item in tabelas:
        if item['nome_tabela'] == nome:
            atributos = pega_conteudo_parenteses(lista_query)
            # for dado in item['dados']:
            #     if dado[0] == atributos[0]:
            #         print("Valor não inserido. ID duplicado.")
            item['dados'].append(atributos)
            item['dados'].sort()
            break
    return tabelas


def verifica_digito(nome):
    """
        Verifica se o nome da tabela não é composto apenas por dígitos.
        Para ser um nome válido, precisa retornar False.

        False: abc, ab2, 2ab
        True: 123, 12.3
    """
    return nome.isdigit()


def pega_conteudo_parenteses(lista_query):
    """
        Separa da query todos os nomes e tipos dos campos da tabela, que ficam entre
        os parênteses.
        Devido a forma de criação da tabela, os itens tem um local fixo para começar e terminar.
    """
    atributos = []
    for item in lista_query[5:-1]:
        if verifica_digito(item):
            atributos.append(int(item))
        else:
            atributos.append(item)
    return atributos


# def verifica_parenteses(abre, fecha):
#     """
#         Verifica se os parênteses foram entrados conforme o esperado.
#         Para ser válido, precisa retornar True.
#     """
#     return abre == '(' and fecha == ')'
