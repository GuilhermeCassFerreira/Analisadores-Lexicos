
# Analisador Léxico - Parte B

## Descrição

Este programa é um analisador léxico que utiliza a biblioteca PLY (Python Lex-Yacc) para ler um arquivo de entrada contendo código-fonte e gerar uma lista de tokens. Ele reconhece identificadores, constantes numéricas, operadores e palavras-chave, além de capturar e sinalizar eventuais erros léxicos.

## Requisitos

- **Python 3.x**

### Instruções para Instalar o Python 3 no Linux

1. Abra o terminal.
2. Atualize a lista de pacotes:
   ```bash
   sudo apt update
   ```
3. Instale o Python 3:
   ```bash
   sudo apt install python3
   ```
4. Verifique a instalação do Python 3:
   ```bash
   python3 --version
   ```

## Instruções de Execução

1. Abra o terminal.
2. Navegue até o diretório onde o arquivo `lexer_parte_b.py` está localizado:
   ```bash
   cd /caminho/para/o/diretorio/Analisadores-Lexicos/parte-b
   ```
3. Execute o seguinte comando:
   ```bash
   python3 lexer_parte_b.py
   ```
4. Quando solicitado, forneça o caminho para o arquivo de entrada com os tokens. Exemplo:
   ```bash
   /caminho/para/o/diretorio/Analisadores-Lexicos/parte-b/entrada_incorreta.lsi
   ```

### Exemplo de Caminho de Arquivos de Entrada

- Para um arquivo de entrada **correto**:
  ```bash
  /caminho/para/o/diretorio/Analisadores-Lexicos/parte-b/entrada_incorreta
  ```
- Para um arquivo de entrada **com erros**:
  ```bash
  /caminho/para/o/diretorio/Analisadores-Lexicos/parte-b/entrada_correta
  ```

### Exemplo Completo de Uso

```bash
python3 lexer_parte_b.py

Forneça o caminho para o arquivo com os tokens: /caminho/para/o/diretorio/Analisadores-Lexicos/parte-b/entrada_incorreta.lsi
```
