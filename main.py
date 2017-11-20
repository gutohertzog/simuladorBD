"""
    Trabalho para simular as transações de um Banco de Dados.

    Estrutura do LOG
    ['start', 'Ti']
    ['t1', 'insert', 'funcionario', '10', 'Fulano', '100']
    ['t1', 'delete', 'funcionario', 'id', '10']

    ...
    ...
    ['end', 'Ti']

    ['Ti', 'del/ins/upd', nome_tabela', 'linha', 'atributo', 'valor_antigo', 'valor_novo']
"""

import menu as m

if __name__ == "__main__":

    m.main_menu()
