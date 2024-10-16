# lexer.py
import ply.lex as lex

# Lista de tokens da gramática X++
tokens = [
    'ID', 'INT', 'FLOAT', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMI', 'COMMA',
    'ASSIGN', 'IF', 'ELSE', 'FOR', 'WHILE', 'RETURN', 'NUMBER'
]

# Palavras reservadas
reserved = {
    'int': 'INT',
    'float': 'FLOAT',
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'while': 'WHILE',
    'return': 'RETURN',
}

# Regras para tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMI = r';'
t_COMMA = r','
t_ASSIGN = r'='

# Regra para números
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

# Regra para identificadores e palavras reservadas
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Verifica se é uma palavra reservada
    return t

# Ignora espaços e tabs
t_ignore = ' \t'

# Conta linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Captura erros léxicos
def t_error(t):
    print(f"Erro léxico: caractere ilegal '{t.value[0]}' na linha {t.lineno}")
    t.lexer.skip(1)

# Cria o lexer
lexer = lex.lex()

# Função para usar o lexer em outro módulo
def get_lexer():
    return lexer
