"""
    Módulo contendo todos os nomes para manipulação da base de dados, das tabelas e das colunas.
    O que está comentado é para uma possível futura implementação.
"""

# variáveis privadas da definição dos termos usados em SQL
_ADD = 'ADD'
_AND = 'AND'
_ALTER = 'ALTER'  #
_ASC = 'ASC'
# _AVG = 'AVG'
# _BETWEEN = 'BETWEEN'
_BY = 'BY'
_CHECKPOINT = 'CHECKPOINT'
_COLUMN = 'COLUMN'
_COMMIT = 'COMMIT'
# _COUNT = 'COUNT'
_CREATE = 'CREATE'
_DATABASE = 'DATABASE'
# _DATE = 'DATE'  # implementar?
_DELETE = 'DELETE'
_DESC = 'DESC'
_DROP = 'DROP'
_FROM = 'FROM'
# _IN = 'IN'
_INSERT = 'INSERT'
_INT = 'INT'
_INTO = 'INTO'
_IS = 'IS'
# _LIKE = 'LIKE'
# _MAX = 'MAX'
# _MIN = 'MIN'
_NOT = 'NOT'
_NULL = 'NULL'
_OR = 'OR'
_ORDER = 'ORDER'
_SELECT = 'SELECT'
_SET = 'SET'
# _SUM = 'SUM'
_TABLE = 'TABLE'
_TOP = 'TOP'
_UPDATE = 'UPDATE'
_VALUES = 'VALUES'
_VARCHAR = 'VARCHAR'
# _VIEW = 'VIEW'  # implementar?
_WHERE = 'WHERE'


# variáveis globais para uso externo

# MANIPULAÇÃO DA BASE DE DADOS
# cria uma nova base de dados SQL
CREATE = _CREATE
DATATABASE = _DATABASE
CREATE_DATABASE = _CREATE + ' ' + _DATABASE
# CREATE DATABASE nome_base_dados

# altera o nome da base de dados
ALTER = _ALTER
ALTER_DATABASE = _ALTER + ' ' + _DATABASE
# ALTER DATABASE nome_base_dados

# deleta a base de dados
DROP = _DROP
DROP_DATABASE = _DROP + ' ' + _DATABASE
# DROP DATABASE nome_base_dados


# MANIPULAÇÃO DAS TABELAS
# cria uma nova tabela
TABLE = _TABLE
CREATE_TABLE = _CREATE + ' ' + _TABLE
# CREATE TABLE nome_tabela (
#     nome_coluna1 tipo_dados,
#     nome_coluna2 tipo_dados,
#     nome_coluna3 tipo_dados,
#    ....
# );

# deleta a tabela
DROP_TABLE = _DROP + ' ' + _TABLE
# DROP TABLE nome_tabela;

# usado para adicionar, deletar ou modificar colunas existentes na tabeka
ALTER_TABLE = _ALTER + ' ' + _TABLE
# Adiciona uma nova coluna à tabela
ADD = _ADD
# ALTER TABLE nome_tabela ADD nome_coluna tipo_dados;
# Deleta uma coluna da tabela
DROP = _DROP
COLUMN = _COLUMN
DROP_COLUMN = _DROP + ' ' + _COLUMN
# ALTER TABLE nome_tabela DROP COLUMN nome_coluna;
# Altera os valores de uma coluna já existente
# ALTER_COLUMN = _ALTER + ' ' + _COLUMN
# ALTER TABLE nome_tabela ALTER COLUMN nome_coluna tipo_dados;


# TIPOS DE DADOS DAS COLUNAS
# tipo de texto genérico
VARCHAR = _VARCHAR
# tipo de número genérico
INT = _INT


# MANIPULADORES DAS TABELAS
# Usado para selecionar dados da tabela.
SELECT = _SELECT
FROM = _FROM
# SELECT * FROM nome_tabela;
# SELECT coluna1, coluna2, ... FROM nome_tabela;

# Usado para filtrar os registros da tabela.
WHERE = _WHERE
# SELECT coluna1, coluna2, ... FROM nome_tabela WHERE condição;

# WHERE pode ser combinado com AND, OR e NOT
# AND e OR podem ser usados como filtro para mais de uma condição.
# O operador AND mostra o registro se todas as condições separadas por AND são TRUE
AND = _AND
# SELECT coluna1, coluna2, ... FROM nome_tabela WHERE condição1 AND condição2 AND condição3;
# O operador OR mostra o registro se qualquer uma das condições separadas por OR for TRUE
OR = _OR
# SELECT coluna1, coluna2, ... FROM nome_tabela WHERE condição1 OR condição2 OR condição3;
# O operador NOT mostra o registro se a(s) condição(ões) não é(são) TRUE
NOT = _NOT
# SELECT coluna1, coluna2, ... FROM nome_tabela WHERE NOT condição;

# Usado para ordenar os resultados ordem ascendente ou descendente.
ORDER_BY = _ORDER + ' ' + _BY
# SELECT coluna1, coluna2, ... FROM nome_tabela ORDER BY coluna1, coluna2, ... ASC|DESC;
# Ordena de forma descendete a(s) coluna(s) selecionada(s).
DESC = _DESC
# SELECT coluna1, coluna2, ... FROM nome_tabela ORDER BY coluna1, coluna2, ... DESC;
# Ordena de forma ascendete a(s) coluna(s) selecionada(s).
ASC = _ASC
# SELECT coluna1, coluna2, ... FROM nome_tabela ORDER BY coluna1, coluna2, ... ASC;

# É usado para inserir novos registros na tabela.
INSERT = _INSERT
INTO = _INTO
INSERT_INTO = _INSERT + ' ' + _INTO
VALUES = _VALUES
# Adicionando valores em colunas específicas
# INSERT INTO nome_tabela (coluna1, coluna3, ...) VALUES (valor1, valor3, ...);
# Adicionando valores em todas as colunas
# INSERT INTO nome_tabela VALUES (valor1, valor2, valor3, ...);

# Usado para adicionar valor vazio ao campo
IS_NULL = _IS + ' ' + _NULL
# SELECT nome_coluna FROM nome_tabela WHERE nome_coluna IS NULL;
# SELECT nome_coluna FROM nome_tabela WHERE nome_coluna IS NOT NULL;

# Usado para modificar um registro já exitente na tabela.
UPDATE = _UPDATE
SET = _SET
# UPDATE nome_tabela SET coluna1 = valor1;
# UPDATE nome_tabela SET coluna1 = valor1, coluna2 = valor2, ... WHERE condição;

# Usado para deletar um registro existente na tabela.
DELETE = _DELETE
# DELETE FROM nome_tabela WHERE condição;

# Usado para especificar o número de registros a ser retornado.
TOP = _TOP
# SELECT TOP número nome_coluna(s) FROM nome_tabela WHERE condição;


# Operações usadas para salvar os dados em disco.
# COMMIT é usado para salvar em disco o log de transações.
COMMIT = _COMMIT
# CHECKPOINT é usado para salvar em disco as tabelas e o log de transações.
CHECKPOINT = _CHECKPOINT
