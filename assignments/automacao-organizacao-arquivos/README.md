# 📘 Assignment: File Organization Automation

## 🎯 Objective

Aprenda a usar Python para automatizar uma tarefa do dia a dia: organizar arquivos de uma pasta em subpastas baseadas em suas extensões. Você praticará caminhos de arquivos, funções, loops, condicionais e tratamento de situações comuns.

## 📝 Tasks

### 🛠️ Explore the Folder

#### Descrição

Implemente uma função que percorra a pasta indicada pelo usuário e identifique os arquivos que precisam ser organizados. Ignore subpastas e o próprio programa.

#### Requisitos

O programa concluído deve:

- Receber o caminho da pasta como argumento de linha de comando
- Listar somente arquivos que estejam diretamente dentro da pasta escolhida
- Exibir o nome de cada arquivo e sua extensão
- Tratar arquivos sem extensão usando a categoria `sem-extensao`

### 🛠️ Organize Files by Extension

#### Descrição

Crie uma subpasta para cada categoria encontrada e mova cada arquivo para a subpasta correspondente. Use `pathlib` e `shutil` da biblioteca padrão do Python.

#### Requisitos

O programa concluído deve:

- Criar as subpastas somente quando forem necessárias
- Usar nomes de extensão sem o ponto e em letras minúsculas, como `pdf`, `jpg` e `txt`
- Mover os arquivos para as subpastas corretas
- Não mover subpastas nem o arquivo `starter-code.py`

### 🛠️ Handle Conflicts and Report Results

#### Descrição

Torne o organizador mais seguro e fácil de usar. Se já existir um arquivo com o mesmo nome na pasta de destino, mantenha o arquivo original no lugar e informe o conflito.

#### Requisitos

O programa concluído deve:

- Evitar sobrescrever arquivos existentes
- Informar quais arquivos foram movidos e quais não foram movidos
- Exibir um resumo final com a quantidade de arquivos movidos e conflitos encontrados
- Mostrar uma mensagem clara quando o caminho informado não existir ou não for uma pasta

#### Exemplo de Uso

```text
python starter-code.py minha-pasta
```

Antes:

```text
minha-pasta/
├── foto.JPG
├── notas.txt
├── roteiro.pdf
└── projeto/
```

Depois:

```text
minha-pasta/
├── jpg/
│   └── foto.JPG
├── pdf/
│   └── roteiro.pdf
├── txt/
│   └── notas.txt
└── projeto/
```
