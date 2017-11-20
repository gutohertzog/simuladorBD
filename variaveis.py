"""
    Módulo responsável por armazenas as variáveis que serão usadas no programa.
"""
import syntax as s

# Variável usada para carregar apenas a primeira vez a tabela do BD.
FLAG = True

# Variáveis responsáveis por armazenar os dados.
# DATABASE = {}
LOG = []
TABELAS = []

# dicionário que vai formatar a transação
# Formato:
# {
#     'transacao': 1,  # campo que vai armazenar a id da transação
#     'lista': []  # lista de operações da transação
# }
# TRANSACAO = {}
# lista de inteiros contendo as transações ainda abertas.
TRANSACOES_ABERTAS = []

# Variável que vai armazenar a transacão aberta.
ATUAL = 0

# Variável que vai armazenar o número mais alto da transação.
ULTIMA = 0

# Tipo de variável aceitável para a criação de tabelas.
TIPO = [s.INT,
        s.VARCHAR
       ]

# Listas contendo os primeiros termos aceitáveis para a execução da query.
TERMO_SIMPLES = [s.SELECT,
                 s.UPDATE,
                 s.DELETE
                ]

TERMO_COMPOSTO = [s.CREATE_DATABASE,
                  s.ALTER_DATABASE,
                  s.DROP_DATABASE,
                  s.CREATE_TABLE,
                  s.ALTER_TABLE,
                  s.DROP_TABLE,
                  s.INSERT_INTO
                 ]

PRIMEIRO_TERMO_COMPOSTO = [s.CREATE,
                           s.ALTER,
                           s.DROP,
                           s.INSERT
                          ]

SEGUNDO_TERMO_COMPOSTO = [s.DATATABASE,
                          s.TABLE,
                          s.INTO
                         ]

TERMO_MEIO = [s.ADD,
              s.DROP,
              s.COLUMN,
              s.VALUES,
              s.WHERE,
              s.FROM
             ]

TERMO_MEIO_COMPOSTO = [s.DROP_COLUMN
                      ]

SALVA = [s.CHECKPOINT,
         s.COMMIT
        ]
