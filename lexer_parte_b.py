import ply.lex as lex

# Lista de tokens
tokens = [
    'ID', 'NUM', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'ASSIGN',
    'LT', 'GT', 'LE', 'GE', 'EQ', 'NE', 'LPAREN', 'RPAREN', 
    'LBRACE', 'RBRACE', 'SEMI', 'COMMA', 'DEF', 'IF', 'ELSE', 
    'PRINT', 'RETURN', 'INT'
]

# Regras regulares para tokens simples
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_ASSIGN  = r':='
t_LT      = r'<'
t_GT      = r'>'
t_LE      = r'<='
t_GE      = r'>='
t_EQ      = r'=='
t_NE      = r'<>'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE  = r'\{'
t_RBRACE  = r'\}'
t_SEMI    = r';'
t_COMMA   = r','

# Regras para palavras-chave
def t_DEF(t):
    r'def'
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_INT(t):
    r'int'
    return t

# Regra para identificadores (variáveis e funções)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

# Regra para constantes numéricas
def t_NUM(t):
    r'\d+'
    t.value = int(t.value)  # Converte o valor para inteiro
    return t

# Ignorar espaços em branco e quebras de linha
t_ignore = ' \t'

# Ignorar comentários
def t_COMMENT(t):
    r'\#.*'
    pass

# Tratamento de erros
def t_error(t):
    print(f"Erro léxico: Caractere inválido '{t.value[0]}' na linha {t.lineno}, coluna {t.lexpos}")
    t.lexer.skip(1)

# Criação do lexer
lexer = lex.lex()

# Função para ler e testar o lexer com um arquivo de entrada
def test_lexer(file_path):
    with open(file_path, 'r') as file:
        input_data = file.read()
    lexer.input(input_data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
            print("Uso: python lexer_parte_b.py <caminho_do_arquivo>")  
    else:
        test_lexer(sys.argv[1])