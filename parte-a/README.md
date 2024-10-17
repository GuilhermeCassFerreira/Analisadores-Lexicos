
# Analisador Léxico - Parte A

## Descrição

Este programa é um analisador léxico, que lê um arquivo de entrada contendo código-fonte e gera uma lista de tokens e uma tabela de símbolos. Ele é baseado em diagramas de transição, reconhecendo identificadores, constantes numéricas e operadores relacionais. Além disso, captura e sinaliza eventuais erros léxicos.

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
2. Navegue até o diretório onde o arquivo `lexer.py` está localizado:
   ```bash
   cd /caminho/para/o/diretorio/Analisadores-Lexicos/parte-a
   ```
3. Execute o seguinte comando:
   ```bash
   python3 lexer.py
   ```
4. Quando solicitado, forneça o caminho para o arquivo de entrada com os tokens. Exemplo:
   ```bash
   /caminho/para/o/diretorio/Analisadores-Lexicos/parte-a/input_incorreto_a
   ```

### Exemplo de Caminho de Arquivos de Entrada

- Para um arquivo de entrada **correto**:
  ```bash
  /caminho/para/o/diretorio/Analisadores-Lexicos/parte-a/input_correto_a
  ```
- Para um arquivo de entrada **com erros**:
  ```bash
  /caminho/para/o/diretorio/Analisadores-Lexicos/parte-a/input_incorreto_a
  ```

### Exemplo Completo de Uso

```bash
python3 lexer.py
Forneça o caminho para o arquivo com os tokens: /caminho/para/o/diretorio/Analisadores-Lexicos/parte-a/input_incorreto_a
```
