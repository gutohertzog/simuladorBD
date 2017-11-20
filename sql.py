"""
    Módulo contendo as manipulações dos menus.
"""

# json vai ser usado para salvar as tabelas em disco
# import json
# import pprint as p
import time
import log as l
import menu as m
import salva as save
import syntax as s
import recover as r
import variaveis as v

from actions import operacao_delete as op_delete
from actions import operacao_insert as op_insert
from actions import operacao_select as op_select
from actions import operacao_update as op_update
# from actions import operacao_create_database as op_c_db
# from actions import operacao_alter_database as op_a_db
# from actions import operacao_drop_database as op_d_db
from actions import operacao_create_table as op_c_t  # OK
# from actions import operacao_alter_table as op_a_t
from actions import operacao_drop_table as op_d_t  # OK


def inicia_sql():
    """
        Inicia o programa SQL.
    """
    if v.FLAG:
        v.TABELAS = save.carrega_tabelas()
        v.ATUAL = int(1)
        v.TRANSACOES_ABERTAS.append(v.ATUAL)
        v.FLAG = False
        temp = []
        temp.append('start')
        temp.append(v.ATUAL)
        v.LOG.append(temp)
        v.ULTIMA = v.ATUAL
    print("Tabelas")
    print(v.TABELAS)
    print("Log")
    print(v.LOG)
    print("Transações Abertas")
    print(v.TRANSACOES_ABERTAS)
    print("Última Transação")
    print(v.ULTIMA)
    print()
    raw_query = le_query()
    query = converte_raw_query(raw_query)
    # primeiro testa se não for para sair.
    if "sair()" in query.lower() or "sair" in query.lower():
        volta_main_menu()
    # encaminha a query para distribui_query
    else:
        distribui_query(query)
        time.sleep(0.5)
        inicia_sql()


def le_query():
    """
        Lê o input do usuário.
    """
    linhas = []
    while True:
        if not linhas:
            line = input("t{} >>> ".format(v.ATUAL))
        else:
            line = input("... ")
        linhas.append(line)
        if ';' in line:
            break
    return linhas


def converte_raw_query(raw_query):
    """
        Converte o input do usuário em uma query de uma linha.
    """
    query = ''
    for item in raw_query:
        if not query:
            query = query + item
        else:
            query = query + " " + item
    return query


def volta_main_menu():
    """
        Encerra o programa SQL e volta para o menu principal.
    """
    print("Todas as alterações não salvas serão permanentemente perdidas.")
    print("Tem certeza que deseja sair?")
    reiterando = input("sim / nao: ")
    if reiterando.lower() == 'sim':
        v.FLAG = True
        m.main_menu()
    else:
        inicia_sql()


def distribui_query(query):
    """
        Recebe a query e a encaminha de acordo com a entrada dos scripts.
    """
    # formata a query
    lista_query = formata_query(query)

    print(lista_query)

    if lista_query[0].upper() == v.SALVA[0]:
        temp = []
        lis = []
        lis = v.TRANSACOES_ABERTAS
        temp.append('checkpoint')
        temp.append(lis)
        v.LOG.append(temp)
        save.checkpoint(v.TABELAS, v.LOG)
    elif lista_query[0].upper() == v.SALVA[1]:
        temp = []
        temp.append('end')
        temp.append(int(v.ATUAL))
        v.LOG.append(temp)
        save.commit(v.LOG)
        # verifica se há apenas uma transação aberta
        if len(v.TRANSACOES_ABERTAS) == 1:
            prox = 0
            prox = v.ULTIMA + 1
            v.ULTIMA = prox
            v.TRANSACOES_ABERTAS.append(prox)
            temp = []
            temp.append('start')
            temp.append(prox)
            v.LOG.append(temp)
        # remove de acordo com o valor
        v.TRANSACOES_ABERTAS.remove(int(v.ATUAL))
        v.ATUAL = v.TRANSACOES_ABERTAS[0]
    # manipula as transações
    elif lista_query[0] == 'start':
        # abre uma nova transação
        if lista_query[1] == 'new':
            v.ATUAL = v.ULTIMA + 1
            v.ULTIMA = v.ATUAL
            v.TRANSACOES_ABERTAS.append(v.ATUAL)
            temp = []
            temp.append('start')
            temp.append(v.ATUAL)
            v.LOG.append(temp)
        # abre uma transação já aberta
        elif lista_query[1].isdigit():
            if int(lista_query[1]) in v.TRANSACOES_ABERTAS:
                v.ATUAL = int(lista_query[1])
            else:
                print("Transação não existe.")
    elif lista_query[0] == 'recover':
        r.separa()
    else:
        manda_query(lista_query)


def manda_query(lista_query):
    """pass"""
    # a menor query tem 3 palavras, então qualquer query para ser validada tem que ter
    # mais que 2 palavras.
    if len(lista_query) > 2:
        # verifica se o primeiro termo faz parte dos termos simples
        if lista_query[0].upper() in v.TERMO_SIMPLES:
            filtro_termo_especifico(lista_query)
        # se não for simples, pode ser composto
        elif lista_query[0].upper() in v.PRIMEIRO_TERMO_COMPOSTO:
            # verifica se o primeiro termo não é o INSERT, pois ele aceita apenas o
            # INTO como segundo termo
            if lista_query[0].upper() == s.INSERT:
                # verifica a única combinação possível para o INSERT
                if lista_query[1].upper() == s.INTO:
                    acao_insert(lista_query)
                # o segundo termo composto não é o INTO
                else:
                    # print("Query incorreta!")
                    print("Segundo termo do INSERT está incorreto")
            # se não for INSERT, então só pode ser CREATE, ALTER ou DROP
            else:
                # verifica se o segundo termo está correto e não é o INTO
                if lista_query[1].upper() in v.SEGUNDO_TERMO_COMPOSTO and \
                lista_query[1].upper() != s.INTO:
                    filtro_termo_composto(lista_query)
                # segundo termo incorreto
                else:
                    print("PRIMEIRO TERMO OK, mas o segundo termo está incorreto!")
        # o primeiro termo está incorreto, não é simples nem composto
        # então não pode ser executado
        else:
            print("Primeiro termo incorreto")
    else:
        print("Termos insuficientes para a execução da query!")
# inicia_sql()


def filtro_termo_especifico(lista_query):
    """
        Separa a query pelo primeiro termo e encaminha para sua respectiva função.
        acao_select(), acao_update() e acao_delete()
    """
    # verifica se o primeiro termo é SELECT
    if s.SELECT in lista_query[0].upper():
        acao_select(lista_query)
    # verifica se o primeiro termo é UPDATE
    elif s.UPDATE in lista_query[0].upper():
        acao_update(lista_query)
    # verifica se o primeiro termo é DELETE
    elif s.DELETE in lista_query[0].upper():
        acao_delete(lista_query)
    else:
        print("Primeiro termo incorreto em filtro!")


def filtro_termo_composto(lista_query):
    """
        Separa a query pelo primeiro e segundo termo e encaminha para sua respectiva função.
        acao_create_database(), acao_alter_database(), acao_drop_database()
        acao_create_table(), acao_alter_table() e acao_drop_table()
    """
    temp = lista_query[0] + ' ' + lista_query[1]
    if s.CREATE_DATABASE in temp.upper():
        print("CREATE DATABASE em desenvolvimento.")
        # acao_create_database(lista_query)
    elif s.ALTER_DATABASE in temp.upper():
        print("ALTER DATABASE em desenvolvimento.")
    elif s.DROP_DATABASE in temp.upper():
        print("DROP DATABASE em desenvolvimento.")
    elif s.CREATE_TABLE in temp.upper():
        acao_create_table(lista_query)
    elif s.ALTER_TABLE in temp.upper():
        print("ALTER TABLE em desenvolvimento.")
		# imcompleto
    elif s.DROP_TABLE in temp.upper():
        acao_drop_table(lista_query)
    else:
        print("Termos incorretos em filtro!")
    return


def acao_select(lista_query):
    """
        Encaminha para o operacao_select.py em actions.
        Lá o sistema irá tratar da operação SELECT.
    """
    if op_select.valida_select(lista_query, v.TERMO_MEIO[5], v.TABELAS):
        if lista_query[1] == '*':
            op_select.retorna_valores(lista_query, v.TABELAS)
        else:
            print("Entrou a seleção de colunas.")


def acao_insert(lista_query):
    """
        Encaminha para o operacao_insert.py em actions.
        Lá o sistema irá tratar da operação INSERT.
    """
    if op_insert.valida_insert(lista_query, v.TERMO_MEIO[3]):
        if op_insert.valida_nomes(lista_query, v.TABELAS):
            v.TABELAS = op_insert.insere(lista_query, v.TABELAS)
            v.LOG.append(l.formata_log_insert(lista_query))
            # v.TRANSACAO['lista'].append(lista_query)
            # print("insert OK")


def acao_update(lista_query):
    """
        Encaminha para o operacao_update.py em actions.
        Lá o sistema irá tratar da operação UPDATE.
    """
    if op_update.valida_update(lista_query, v.TABELAS):
        v.TABELAS, valor_velho = op_update.atualiza(lista_query, v.TABELAS)
        v.LOG.append(l.formata_log_update(lista_query, valor_velho))
        # v.TRANSACAO['lista'].append(lista_query)
        # print("Update OK!")


def acao_delete(lista_query):
    """
        Encaminha para o operacao_delete.py em actions.
        Lá o sistema irá tratar da operação DELETE.
    """
    if op_delete.valida_delete(lista_query, v.TERMO_MEIO[4]):
        if op_delete.valida_nomes(lista_query[2], v.TABELAS):
            v.TABELAS = op_delete.deleta_registro(lista_query, v.TABELAS)
            v.LOG.append(l.formata_log_delete(lista_query))
            # v.TRANSACAO['lista'].append(lista_query)


# def acao_create_database(lista_query):
#     """
#         pass
#     """
#     # verifica se a query está ok
#     if op_c_db.valida_create_database(lista_query):
#         # pega os nomes de todas as database
#         nomes_database = list(v.DATABASE.keys())
#         # verifica se o nome já não está sendo usado na database
#         if op_c_db.verifica_nome(lista_query[2], nomes_database):
#             v.DATABASE[lista_query[2]] = {}
#         else:
#             print("Esse nome já está sendo usado como nome de uma database")
#     return


# def acao_alter_database(lista_query):
#     """
#         pass
#     """
#     op_a_db.main_alter_database(lista_query)


# def acao_drop_database(lista_query):
#     """
#         pass
#     """
#     op_d_db.main_drop_database(lista_query)


def acao_create_table(lista_query):
    """
        Função que vai chamar as validações e criações da Table
    """
    if op_c_t.valida_create_table(lista_query, v.TIPO):
        if op_c_t.verifica_nome(lista_query[2], v.TABELAS):
            v.TABELAS.append(op_c_t.cria_tabela(lista_query))
            v.LOG.append(l.formata_log_create_table(lista_query))
            # v.TRANSACAO['lista'].append(lista_query)


# def acao_alter_table(lista_query):
#     """
#         EM DESENVOLVIMENTO.
#     """
#     if op_a_t.valida_alter_table(lista_query, v.TABELAS):
#         if op_a_t.valida_add(lista_query, v.TERMO_MEIO, v.TIPO):
#             pass
#         elif op_a_t.valida_drop(lista_query, v.TERMO_MEIO):
#             pass
#         # print("Alter ok")


def acao_drop_table(lista_query):
    """
        PRONTO!
        pass
    """
    if op_d_t.valida_drop_table(lista_query):
        if op_d_t.verifica_nome(lista_query[2], v.TABELAS):
            del v.TABELAS[op_d_t.deleta_tabela(lista_query[2], v.TABELAS)]
            v.LOG.append(l.formata_log_drop_table(lista_query))


def formata_query(query):
    """
        Função resposável por retirar ; da string (item obrigatório para executar a query).
        Passar por toda a query e adicionar um espaço antes e depois de cada parênteses e vírgulas.
        Dividir a query em uma lista usando os espaços como parâmetro.
        Remover da lista todos os itens vazios.
    """
    # remove ; e , da query
    query = query.replace(";", " ")
    query = query.replace(",", " ")
    # coloca espaço antes e depois dos parênteses e vírgulas
    temp = ''
    for item in query:
        if '(' in item:
            temp = temp + " " + item + " "
        elif ')' in item:
            temp = temp + " " + item + " "
        # elif ',' in item:
        #     temp = temp + " " + item + " "
        else:
            temp = temp + item
    # divide a query em uma lista usando o espaço como separador
    lista_query = temp.split(' ')
    # remove da lista os itens da lista vazios
    lista_query = list(filter(None, lista_query))
    return lista_query
