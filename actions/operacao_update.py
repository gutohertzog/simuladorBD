"""
    Módulo responsável por realizar as operações de validação e execução com o UPDATE.

    Sintaxe para atualização dos dados.
    UPDATE nome_tabela
        SET coluna_valor = valor
        WHERE coluna_chave = chave;
"""


def valida_update(lista_query, tabelas):
    """
        pass
    """
    if valida_nomes(lista_query, tabelas):
        return False
    if valida_set_where(lista_query):
        print("Não foram encontrados SET e/ou WHERE")
        return False
    return True


def atualiza(lista_query, tabelas):
    """
        pass
    """
    nome_tabela = lista_query[1]
    nome_valor = lista_query[3]
    valor = lista_query[5]
    coluna_chave = lista_query[7]
    chave = lista_query[-1]
    valor_velho = 0
    for item in tabelas:
        if item['nome_tabela'] == nome_tabela:
            i_val = item['coluna_nome'].index(nome_valor)
            if item['coluna_tipo'][i_val] == 'int':
                valor = int(valor)
            i_cha = item['coluna_nome'].index(coluna_chave)
            if item['coluna_tipo'][i_cha] == 'int':
                chave = int(chave)
            # pass
            # trocar = []
            for indice, dado in enumerate(item['dados']):
                if dado[i_cha] == chave:
                    # trocar = dado
                    valor_velho = dado[i_val]
                    dado[i_val] = valor
                    # ind_apagar = indice
                    # del item['dados'][ind_apagar]
                    break
            # print(indice)
            # print("Entrou em ATUALIZAR!")
            break
            # pass
    return tabelas, valor_velho


def valida_nomes(lista_query, tabelas):
    """
        Verifica se o nome das tabela está correto e se os campos estão corretos também.

        Para ser válido, precisa retornar False.
    """
    nome_tabela = lista_query[1]
    nome_coluna1 = lista_query[3]
    chave1 = lista_query[5]
    nome_coluna2 = lista_query[7]
    chave2 = lista_query[-1]
    for item in tabelas:
        # print(item['nome_tabela'])
        # print(nome_tabela)
        if item['nome_tabela'] == nome_tabela:
            if nome_coluna1 in item['coluna_nome']:
                if nome_coluna2 in item['coluna_nome']:
                    i = item['coluna_nome'].index(nome_coluna1)
                    if item['coluna_tipo'][i] == 'int':
                        chave1 = int(chave1)
                    i = item['coluna_nome'].index(nome_coluna2)
                    if item['coluna_tipo'][i] == 'int':
                        chave2 = int(chave2)
                    # print(chave1)
                    # print(chave2)
                    for dado in item['dados']:
                        print(dado)
                        print(item['dados'])
                        if chave2 in dado:
                            return False
                        # else:
                    print("Registro não encontrado!")
                    return True
                else:
                    print("Coluna não encontrada!")
                    return True
            else:
                print("Coluna não encontrada!")
                return True
    print("Tabela não encontrada!")
    return True


def valida_set_where(lista_query):
    """
        pass
    """
    if lista_query[-4].upper() not in 'WHERE':
        return True
    if lista_query[2].upper() not in 'SET':
        return True
    return False
