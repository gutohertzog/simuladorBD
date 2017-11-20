"""
    pass
"""

import json

def checkpoint(tabelas, log):
    """
        pass
    """
    salva_log(log)
    salva_checkpoint(tabelas)

def commit(log):
    """
        pass
    """
    salva_log(log)

def carrega_tabelas():
    """
        pass
    """
    nome = "banco_de_dados.json"
    with open(nome) as arq:
        print("Base de dados Carregada.")
        return json.load(arq)

def salva_checkpoint(tabelas):
    """pass
    https://stackoverflow.com/questions/13249415/can-i-implement-custom-indentation-for-pretty-printing-in-python-s-json-module
    """
    nome = "banco_de_dados.json"
    modo = 'w'
    with open(nome, modo) as arq:
        json.dump(tabelas, arq, indent=4)
    print("Base de dados Salva.")


def salva_log(log):
    """pass"""
    nome = "log.json"
    modo = 'w'
    with open(nome, modo) as arq:
        json.dump(log, arq, indent='\t')
    print("Log salvo!")
    # pass
