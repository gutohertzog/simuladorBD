"""
    Módulo responsável por realizar as operações de validação e execução com o DELETE.

    Sintaxe para criação da table:
    DELETE FROM nome_tabela
        WHERE coluna = condição;
"""

# from pprint import pprint


def valida_delete(lista_query, termo_meio):
    """
        pass
    """
    if verifica_digito(lista_query[2]):
        print("O nome da tabela não pode ser dígitos.")
        return False
    if termo_meio not in lista_query[3].upper():
        return False
    # print(lista_query)
    return True


def valida_nomes(nome, tabelas):
    """
        Verifica se o nome das tabela está correto.

        Para ser válido, precisa retornar True.
    """
    for item in tabelas:
        if item['nome_tabela'] == nome:
            return True
    print("Tabela inexistente.")
    return False


def deleta_registro(lista_query, tabelas):
    """
        pass
    """
    nome_tabela = lista_query[2]
    coluna = lista_query[4]
    chave = lista_query[6]
    # print(lista_query)

    for item in tabelas:
        if item['nome_tabela'] == nome_tabela:
            if coluna in item['coluna_nome']:
                i = item['coluna_nome'].index(coluna)
                # print(item['coluna_tipo'][i])
                if item['coluna_tipo'][i] == 'int':
                    chave = int(chave)
                # pprint(chave)
                ind_apagar = 0
                # print(i)
                for indice, dado in enumerate(item['dados']):
                    if dado[i] == chave:
                        ind_apagar = indice
                        del item['dados'][ind_apagar]
                        break
                break
            else:
                print("Coluna não encontrada.")
    return tabelas


def verifica_digito(nome):
    """
        Verifica se o nome da tabela não é composto apenas por dígitos.
        Para ser um nome válido, precisa retornar False.

        False: abc, ab2, 2ab
        True: 123, 12.3
    """
    return nome.isdigit()
