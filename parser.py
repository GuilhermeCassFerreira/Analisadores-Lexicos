# parser.py
import ply.yacc as yacc
from lexer import tokens, get_lexer  # Importa os tokens e o lexer do arquivo lexer.py

# Regras de produção da gramática X++

# Regra para um programa
def p_program(p):
    'program : declarations statements'
    pass

# Regra para declarações
def p_declarations(p):
    '''declarations : declarations declaration
                    | empty'''
    pass

# Regra para uma única declaração
def p_declaration(p):
    '''declaration : INT ID SEMI
                   | FLOAT ID SEMI'''
    pass

# Regra para expressões
def p_expression(p):
    '''expression : expression PLUS term
                  | expression MINUS term
                  | term'''
    pass

# Regra para termos
def p_term(p):
    '''term : term TIMES factor
            | term DIVIDE factor
            | factor'''
    pass

# Regra para fatores
def p_factor(p):
    '''factor : NUMBER
              | ID
              | LPAREN expression RPAREN'''
    pass

# Regra para comandos (statements)
def p_statements(p):
    '''statements : statements statement
                  | empty'''
    pass

# Regra para um comando individual
def p_statement(p):
    '''statement : assignment
                 | if_statement
                 | return_statement'''
    pass

# Regra para atribuições
def p_assignment(p):
    '''assignment : ID ASSIGN expression SEMI'''
    pass

# Regra para estrutura de controle (if)
def p_if_statement(p):
    '''if_statement : IF LPAREN expression RPAREN LBRACE statements RBRACE else_clause'''
    pass

# Regra para else opcional
def p_else_clause(p):
    '''else_clause : ELSE LBRACE statements RBRACE
                   | empty'''
    pass

# Regra para return
def p_return_statement(p):
    '''return_statement : RETURN expression SEMI'''
    pass

# Regra para vazio (empty)
def p_empty(p):
    'empty :'
    pass

# Função de erro sintático
def p_error(p):
    if p:
        print(f"Erro de sintaxe no token '{p.value}' na linha {p.lineno}")
    else:
        print("Erro de sintaxe no final do arquivo")

# Cria o parser
parser = yacc.yacc()

# Função para analisar o arquivo de entrada
def analisar_arquivo(arquivo):
    lexer = get_lexer()  # Obtém o lexer do arquivo lexer.py
    with open(arquivo, 'r') as f:
        data = f.read()
        result = parser.parse(data, lexer=lexer)
        if result is None:
            print("Análise sintática completa sem erros.")
        else:
            print("Análise completa.")

# Função principal
if __name__ == "__main__":
    arquivo = 'entrada.txt'  # Nome do arquivo que contém a entrada
    analisar_arquivo(arquivo)
