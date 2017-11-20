"""pass"""

import json
import sql as sql
# import variaveis as v


def separa():
    """pass"""
    nome = "log.json"
    # modo = 'r'
    with open(nome) as arq:
        log = json.load(arq)
        # print(log)
    # 1. Aloca duas listas: lista-UNDO e lista-REDO
    lista_undo = []
    lista_redo = []
    # 2. Percorre o arquivo de LOG do fim para o início até chegar ao primeiro
    # registro de checkpoint, examinando cada registro:
    for item in reversed(log):
        # 2.1. se achou <Fim Ti>, adiciona Ti na lista-REDO
        if item[0] == 'end':
            lista_redo.append(item[1])
        # 2.2. se achou <Inicio Ti> e Ti não está na lista-REDO, adiciona Ti na lista-UNDO
        elif item[0] == 'start' and item[1] not in lista_redo:
            lista_undo.append(item[1])
        # 3. Quando se chega ao registro checkpoint, para cada transação Ti na
        # lista de transações desse registro:
        elif item[0] == 'checkpoint':
            for i in item[1]:
                # 3.1. se Ti não estiver na lista-REDO, então adiciona Ti na lista-UNDO
                if i not in lista_redo:
                    lista_undo.append(i)
            break
    print("lista undo {}".format(lista_undo))
    print("lista redo {}".format(lista_redo))
    input("Press Enter to continue...")
    # 4. Percorre o arquivo de LOG do fim para o início:
    for item in reversed(log):
        # 4.1. realizando UNDO(Ti) para todas as transações Ti existentes na lista-UNDO
        if item[0] in lista_undo:
            executa_undo(item)
            input("Press Enter to continue...")
            # pass
        # 4.2. marcando na lista-REDO as transações Ti cujos registros <Início Ti> estão
        # sendo encontrados nessa varredura
        elif item[0] == 'start':
            if int(item[1]) not in lista_undo:
                if int(item[1]) not in lista_redo:
                    lista_redo.append(item[1])
    # 6. Percorre o arquivo de LOG para a frente, realizando REDO(Ti) para todas as transações
    # existentes na lista-REDO.
    for item in log:
        if item[0] in lista_redo:
            executa_redo(item)
            input("Press Enter to continue...")
            # pass
    # print("lista undo {}".format(lista_undo))
    # print("lista redo {}".format(lista_redo))
    input("Press Enter to continue...")


def executa_undo(item):
    """pass"""
    lista_query = []
    if item[1] == 'delete':
        print("Delete undo em desenvolvimento!")
    if item[1] == 'insert':
        print("Insert undo em desenvolvimento!")
    elif item[1] == 'update':
        # UPDATE nome_tabela
        #     SET coluna_valor = valor
        #     WHERE coluna_chave = chave;
        lista_query.append('update')
        lista_query.append(item[2])
        lista_query.append('set')
        lista_query.append(item[3])
        lista_query.append('=')
        lista_query.append(item[7])
        lista_query.append('where')
        lista_query.append(item[5])
        lista_query.append('=')
        lista_query.append(item[6])
    elif item[1] == 'create':
        print("Create table undo em desenvolvimento!")
    elif item[1] == 'drop':
        print("Drop Table undo em desenvolvimento!")
    print("lista_query UNDO: {}".format(lista_query))
    # sql.manda_query(lista_query)


def executa_redo(item):
    """pass"""
    lista_query = []
    if item[1] == 'delete':
        # DELETE FROM nome_tabela
        #     WHERE coluna = condição;
        lista_query.append(item[1])
        lista_query.append('from')
        lista_query.append(item[2])
        lista_query.append('where')
        lista_query.append(item[3])
        lista_query.append('=')
        lista_query.append(item[4])
        # print(lista_query)
    elif item[1] == 'insert':
        # INSERT INTO nome_tabela VALUES (
        #     valor1,
        #     valor2,
        #     valor3,
        #     ...
        # );
        lista_query.append(item[1])
        lista_query.append('into')
        lista_query.append(item[2])
        lista_query.append('values')
        lista_query.append('(')
        for i in item[3]:
            lista_query.append(i)
        lista_query.append(')')
        # print(lista_query)
    elif item[1] == 'update':
        # UPDATE nome_tabela
        #     SET coluna_valor = valor
        #     WHERE coluna_chave = chave;
        lista_query.append(item[1])
        lista_query.append(item[2])
        lista_query.append('set')
        lista_query.append(item[3])
        lista_query.append('=')
        lista_query.append(item[4])
        lista_query.append('where')
        lista_query.append(item[5])
        lista_query.append('=')
        lista_query.append(item[6])
        # print(lista_query)
    elif item[1] == 'create':
        # CREATE TABLE nome_tabela (
        #     nome_coluna1 tipo_dados,
        #     nome_coluna2 tipo_dados,
        #     nome_coluna3 tipo_dados
        #     ....
        # );
        lista_query.append(item[1])
        lista_query.append('table')
        lista_query.append(item[2])
        lista_query.append('(')
        for i in item[3]:
            lista_query.append(i)
        lista_query.append(')')
        # print(lista_query)
    elif item[1] == 'drop':
        lista_query.append(item[1])
        lista_query.append(item[2])
        lista_query.append(item[3])
        # print(lista_query)
    print("lista_query REDO: {}".format(lista_query))
    # sql.manda_query(lista_query)
