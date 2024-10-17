import sys

class Token:
    def __init__(self, type_, value, position):
        self.type = type_
        self.value = value
        self.position = position

    def __repr__(self):
        return f"Token(type={self.type}, value={self.value}, position={self.position})"

class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.position = 0
        self.tokens = []

    def advance(self):
        self.position += 1

    def peek(self):
        if self.position < len(self.source_code):
            return self.source_code[self.position]
        return None

    def lex(self):
        while self.position < len(self.source_code):
            current_char = self.peek()

            # Ignorar espaços em branco
            if current_char.isspace():
                self.advance()
                continue

            # Identificador
            if current_char.isalpha():
                self.tokens.append(self.lex_identifier())
                continue

            # Constante Numérica
            if current_char.isdigit():
                self.tokens.append(self.lex_number())
                continue

            # Operadores Relacionais
            if current_char in ('<', '>', '=', '!'):
                self.tokens.append(self.lex_relational_operator())
                continue

            # Caractere não reconhecido
            raise ValueError(f"Caractere não reconhecido na posição {self.position}: {current_char}")

        return self.tokens

    def lex_identifier(self):
        start_position = self.position
        lexeme = self.peek()

        self.advance()
        while self.peek() is not None and self.peek().isalnum():
            lexeme += self.peek()
            self.advance()

        return Token(type_="IDENTIFIER", value=lexeme, position=start_position)

    def lex_number(self):
        start_position = self.position
        lexeme = self.peek()

        self.advance()
        while self.peek() is not None and self.peek().isdigit():
            lexeme += self.peek()
            self.advance()

        return Token(type_="INTEGER", value=int(lexeme), position=start_position)

    def lex_relational_operator(self):
        start_position = self.position
        lexeme = self.peek()

        self.advance()
        if lexeme in ('<', '>') and self.peek() is not None and self.peek() == '=':
            lexeme += self.peek()
            self.advance()
        elif lexeme == '!' and self.peek() is not None and self.peek() == '=':
            lexeme += self.peek()
            self.advance()

        if lexeme not in ('<', '>', '=', '<=', '>=', '!='):
            raise ValueError(f"Operador relacional inválido na posição {start_position}: {lexeme}")

        return Token(type_="RELATIONAL_OPERATOR", value=lexeme, position=start_position)

def read_file(filename):
    """Lê o conteúdo de um arquivo e retorna como uma string."""
    with open(filename, 'r') as file:
        return file.read()

def main():
    # Verifica se o argumento do arquivo foi passado
    if len(sys.argv) < 2:
        print("Uso: python lexer.py <nome_do_arquivo>")
        sys.exit(1)

    # Lê o nome do arquivo de entrada
    input_filename = sys.argv[1]

    try:
        # Lê o conteúdo do arquivo
        source_code = read_file(input_filename)

        # Executa o analisador léxico
        lexer = Lexer(source_code)
        tokens = lexer.lex()

        # Imprime os tokens gerados
        print("Tokens encontrados:")
        for token in tokens:
            print(token)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{input_filename}' não foi encontrado.")
    except ValueError as e:
        print(f"Erro durante a análise léxica: {e}")

if __name__ == "__main__":
    main()
