# Bruno Vazquez Lafaiete (20102277), Guilherme Cassiano Ferreira Silva (23250871), Victor Luiz de Souza (21105576)
import os
class Token:
    def __init__(self, tag):
        self.tag = tag

    def __str__(self):
        return f"<{self.tag}>"

class Num(Token):
    def __init__(self, value):
        super().__init__('NUM')
        self.value = value

    def __str__(self):
        return f"<{self.tag}, {self.value}>"

class Word(Token):
    def __init__(self, tag, lexeme):
        super().__init__(tag)
        self.lexeme = lexeme

    def __str__(self):
        return f"<{self.tag}, '{self.lexeme}'>"

class Relop(Token):
    def __init__(self, tag, operator):
        super().__init__(tag)
        self.operator = operator

    def __str__(self):
        return f"<{self.tag}, '{self.operator}'>"

class ErrorToken(Token):
    def __init__(self, message, nlin, ncol):
        super().__init__('ERROR')
        self.message = message
        self.nlin = nlin
        self.ncol = ncol

    def __str__(self):
        return f"Erro léxico na linha {self.nlin}, coluna {self.ncol}: {self.message}"

class InputBuffer:
    def __init__(self, input_data):
        self.data = input_data
        self.pos = 0
        self.nlin = 1
        self.ncol = 1

    def peek(self):
        if self.pos < len(self.data):
            return self.data[self.pos]
        else:
            return None  #fim do arquivo

    # mesmo sentido do "get"
    def advance(self):
        if self.pos < len(self.data):
            ch = self.data[self.pos]
            self.pos += 1
            if ch == '\n':
                self.nlin += 1
                self.ncol = 1
            else:
                self.ncol += 1
            return ch
        else:
            return None  #fim do arquivo

class Lexer:
    def __init__(self, input_data):
        self.input = InputBuffer(input_data)
        self.words = {}
        self.tokens = []
        # considera IF, THEN e ELSE como palavras reservadas
        self.reserve(Word('IF', 'if'))
        self.reserve(Word('THEN', 'then'))
        self.reserve(Word('ELSE', 'else'))

        self.p = self.input.peek()

    def reserve(self, word):
        self.words[word.lexeme] = word

    def scan(self):
        #ao entrar, ignora o espaço em branco ou quebra de linha.
        while True:
            if self.p == ' ' or self.p == '\t':
                self.input.advance()
                self.p = self.input.peek()
            elif self.p == '\n':
                self.input.advance()
                self.p = self.input.peek()
            else:
                break
        if self.p is None:
            return None  #fim do arquivo
        if self.p in ('<', '=', '>'):
            return self.simula_AFD_RELOPS()
        elif self.p.isdigit():
            return self.simula_AFD_NUMS()
        elif self.p.isalpha():
            return self.simula_AFD_IDS()
        else:
            #caracteres nao reconhecidos por RELOP, nem NUMS nem IDs
            return self.simula_OUTRO()

    def simula_AFD_RELOPS(self):
        #seguindo o exemplo e o diagrama de transição de RELOPs fornecido em aula
        state = 0
        accept = False
        resp = None
        while True:
            if state == 0:
                if self.p == '<':
                    self.input.advance()
                    self.p = self.input.peek()
                    state = 1
                elif self.p == '=':
                    self.input.advance()
                    self.p = self.input.peek()
                    state = 5
                elif self.p == '>':
                    self.input.advance()
                    self.p = self.input.peek()
                    state = 6
                else:
                    break
            elif state == 1:
                if self.p == '=':
                    self.input.advance()
                    self.p = self.input.peek()
                    state = 2
                elif self.p == '>':
                    self.input.advance()
                    self.p = self.input.peek()
                    state = 3
                elif self.p == '<':
                    #se tiver '<<' retorna erro
                    nlin = self.input.nlin
                    ncol = self.input.ncol
                    message = f"Operador inválido '<<'"
                    return ErrorToken(message, nlin, ncol)
                else:
                    state = 4
            elif state == 6:
                if self.p == '=':
                    self.input.advance()
                    self.p = self.input.peek()
                    state = 7
                elif self.p == '>':
                    #se tiver '>>' retorna erro
                    nlin = self.input.nlin
                    ncol = self.input.ncol
                    message = f"Operador inválido '>>'"
                    return ErrorToken(message, nlin, ncol)
                else:
                    state = 8
            elif state == 2:
                resp = Relop('RELOP', '<=')
                accept = True
            elif state == 3:
                resp = Relop('RELOP', '!=')
                accept = True
            elif state == 4:
                resp = Relop('RELOP', '<')
                accept = True
            elif state == 5:
                resp = Relop('RELOP', '=')
                accept = True
            elif state == 7:
                resp = Relop('RELOP', '>=')
                accept = True
            elif state == 8:
                resp = Relop('RELOP', '>')
                accept = True
            if accept:
                self.tokens.append(resp)
                return resp

    def simula_AFD_NUMS(self):
        v = 0
        while True:
            v = v * 10 + int(self.p)
            self.input.advance()# consome o caractere
            self.p = self.input.peek()# espia o proximo caractere
            if self.p is None or not self.p.isdigit(): #se for digito volta pro laço
                break
        if self.p is not None and self.p.isalpha():
            #digito seguido de caracteres nao numericos
            nlin = self.input.nlin
            ncol = self.input.ncol
            message = f"Caractere inesperado '{self.p}' após número"
            return ErrorToken(message, nlin, ncol)
        num_token = Num(v)
        self.tokens.append(num_token) #adiciona na lista de tokens
        return num_token

    def simula_AFD_IDS(self):
        buf = ''
        while True:
            buf += self.p
            self.input.advance() # consome o caractere
            self.p = self.input.peek() # espia o proximo caractere
            if self.p is None or not self.p.isalnum(): #se for numero ou digito volta pro laço
                break
        s = buf
        # logica p/ verificar se ja esta presente na tabela de simbolos, senão, adiciona
        if s in self.words:
            token = self.words[s]
        else:
            token = Word('ID', s)
            self.words[s] = token
        self.tokens.append(token) #adiciona na lista de tokens
        return token

    def simula_OUTRO(self):
        ch = self.p
        nlin = self.input.nlin
        ncol = self.input.ncol
        message = f"Caractere inesperado '{ch}'"
        return ErrorToken(message, nlin, ncol)

    def get_tokens(self):
        return self.tokens

    def get_symbol_table(self):
        #logica para excluir as palavras chaves da tabela de simbolo
        symbol_table = {lex.lexeme: lex for lex in self.words.values() if lex.tag == 'ID'}
        return symbol_table

def main():
    filename = input("Forneça o caminho para o arquivo com os tokens: ")
    filename = os.path.expanduser(filename)
    filename = os.path.abspath(filename)
    try:
        with open(filename, 'r') as file:
            input_data = file.read()
    except FileNotFoundError:
        print(f"Arquivo '{filename}' não encontrado.")
        return
    lexer = Lexer(input_data)
    tokens = []
    has_error = False
    error_message = ''
    while True:
        token = lexer.scan()
        if token is None:
            break #sai do laço no fim do arquivo
        if isinstance(token, ErrorToken):
            has_error = True
            error_message = str(token)
            break #sai do laço ao existir uma mensagem de erro
        else:
            tokens.append(token)
    if has_error:
        #se tem erro printa apenas a mensagem de erro, senão printa a lista de tokens e a tabela de simbolos
        print(error_message)
    else:
        print("Lista de tokens:")
        for token in tokens:
            print(token)
        print("\nTabela de símbolos:")
        symbol_table = lexer.get_symbol_table()
        for lexeme, token in symbol_table.items():
            print(f"{lexeme}: {token.tag}")

if __name__ == '__main__':
    main()
