"""
    Módulo contendo as manipulações dos menus.
"""

import os
import sys
import time
import sql
import instrucoes as i


def apresentacao():
    """
        Cabeçalho de apresentação do trabalho.
    """
    print("\n\t\t\tGreetings, stranger!\n")
    print("\t\tSimulador de SQL para Simular Falhas\n\n")
    print("\t\t\t     Autor")
    print("\t\t\t   Augusto Hertzog\n")
    return


def limpa_tela():
    """
        Função responsável por limpar a tela, independente do sistema operacional.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    return


def main_menu():
    """
        Menu principal, que vai lidar com o programa.
    """
    limpa_tela()
    apresentacao()
    print("O que você quer fazer?\n")
    print("\t1. Iniciar o programa")
    print("\t2. Instruções")
    print("\t0. Sair")
    escolha = input("\n >>  ")

    # menu de escolha
    if escolha == '1':
        inicia_sql()
    elif escolha == '2':
        instrucoes()
    elif escolha == '0':
        sair()
    else:
        limpa_tela()
        print("\n\n\t\t\tSeleção inválida. Escolha novamente.\n")
        time.sleep(3)
        main_menu()
    return


def instrucoes():
    """
        Vai carregar um arquivo de texto contendo as explicações de como funciona o programa.
    """
    limpa_tela()
    i.instrucoes()
    print("\n\n\t9. Voltar")
    escolha = input("\n >>  ")

    # menu de escolha
    if escolha == '9':
        main_menu()
    else:
        limpa_tela()
        print("\n\n\t\t\tSeleção inválida. Escolha novamente.\n")
        time.sleep(3)
        instrucoes()
    return


def inicia_sql():
    """
        Inicia a aplicação de SQL para simular as falhas.
    """
    limpa_tela()
    print("\n\n\t\tIniciando o SQL\n")
    print("\nDigite sair() para sair do programa e voltar ao menu principal.")
    print("\nTodas as alterações não salvas serão perdidas.\n\n")
    time.sleep(1)
    limpa_tela()
    sql.inicia_sql()
    return


def sair():
    """
        Termina com a aplicação.
    """
    limpa_tela()
    print("\n\n\t\t\tAté a próxima, Stranger.\n\n")
    time.sleep(1)
    limpa_tela()
    sys.exit()
    return
