"""pass"""

import variaveis as v


def formata_log_delete(lista_query):
    """pass"""
    formatado = []
    formatado.append(v.ATUAL)  # código da transação
    formatado.append(lista_query[0])  # nome da transação
    formatado.append(lista_query[2])  # nome da tabela
    formatado.append(lista_query[4])  # nome da coluna
    if lista_query[6].isdigit():
        formatado.append(int(lista_query[6]))  # nome da condição
    else:
        formatado.append(lista_query[6])  # nome da condição
    return formatado


def formata_log_insert(lista_query):
    """pass"""
    formatado = []
    formatado.append(v.ATUAL)  # código da transação
    formatado.append(lista_query[0])  # nome da transação
    formatado.append(lista_query[2])  # nome da tabela
    atributos = []  # vai armazenar os atributos
    for item in lista_query[5:-1]:
        if item.isdigit():
            atributos.append(int(item))
        else:
            atributos.append(item)
    formatado.append(atributos)  # valores a serem inseridos na tabela
    return formatado


def formata_log_update(lista_query, valor_velho):
    """pass"""
    formatado = []
    formatado.append(v.ATUAL)  # código da transação
    formatado.append(lista_query[0])  # nome da transação
    formatado.append(lista_query[1])  # nome da tabela
    formatado.append(lista_query[3])  # nome da coluna_valor
    if lista_query[5].isdigit():
        formatado.append(int(lista_query[5]))  # valor a ser alterado em coluna_valor
    else:
        formatado.append(lista_query[5])  # valor a ser alterado em coluna_valor
    formatado.append(lista_query[7])  # nome da coluna_chave
    if lista_query[9].isdigit():
        formatado.append(int(lista_query[9]))  # valor_chave a ser buscado em coluna_valor
    else:
        formatado.append(lista_query[9])  # valor_chave a ser buscado em coluna_valor
    if valor_velho.isdigit():
        formatado.append(int(valor_velho))  # valor antigo do update
    else:
        formatado.append(valor_velho)  # valor antigo do update
    return formatado


def formata_log_create_table(lista_query):
    """pass"""
    formatado = []
    formatado.append(v.ATUAL)  # código da transação
    formatado.append(lista_query[0])  # nome da transação
    formatado.append(lista_query[2])  # nome da tabela
    atributos = []
    for item in lista_query[4:-1]:
        atributos.append(item)
    formatado.append(atributos)  # valores a serem inseridos na tabela
    return formatado


def formata_log_drop_table(lista_query):
    """pass"""
    formatado = []
    formatado.append(v.ATUAL)  # código da transação
    formatado.append(lista_query[0])  # nome da transação
    formatado.append(lista_query[1])  # nome da transação
    formatado.append(lista_query[2])  # nome da tabela
    return formatado
