# API de Catálogo de Livros com Python e Flask

Atividade prática avaliativa da disciplina **Programação — Web Coding** (AV2 - Revisão 1).

---

## 1. Objetivo da API

O objetivo desta aplicação é fornecer uma API REST mínima utilizando Python e o microframework Flask. A aplicação disponibiliza um catálogo inicial com três livros cadastrados em formato JSON, permitindo a integração e consulta por outros sistemas através de uma requisição HTTP do tipo `GET`.

---

## 2. Tecnologias Utilizadas

- **Python 3**
- **Flask** (Microframework Web)

---

## 3. Estrutura do Projeto

```text
api-livros/
├── app.py              # Código principal da aplicação Flask
├── requirements.txt    # Lista de dependências do projeto
├── README.md           # Documentação completa
└── .gitignore          # Arquivos e diretórios ignorados pelo Git
```

---

## 4. Instruções para Instalar as Dependências

### 4.1. Criar o ambiente virtual

Abra o terminal na pasta do projeto e execute:

```bash
# Windows
python -m venv venv

# Linux / macOS
python3 -m venv venv
```

### 4.2. Ativar o ambiente virtual

```bash
# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Windows (Prompt de Comando - CMD)
venv\Scripts\activate.bat

# Linux / macOS
source venv/bin/activate
```

### 4.3. Instalar o Flask

Com o ambiente virtual ativado:

```bash
pip install -r requirements.txt
```
*(ou diretamente via `pip install Flask`)*

---

## 5. Instruções para Executar a Aplicação

Com o ambiente virtual ativado, inicie o servidor com o comando:

```bash
python app.py
```

O servidor será iniciado localmente no endereço padrão:
`http://127.0.0.1:5000` (ou `http://localhost:5000`).

---

## 6. Endereço da Rota Disponibilizada

- **Rota:** `/livros`
- **Método HTTP:** `GET`
- **URL Completa:** [http://127.0.0.1:5000/livros](http://127.0.0.1:5000/livros)

### Exemplo de Resposta esperada (JSON):

```json
{

  "livros": [
    {
        "id": 1,
        "titulo": "Jogos Vorazes",
        "autor": "Suzanne Collins",
        "ano": 2008
    },
    {
        "id": 2,
        "titulo": "A Seleção",
        "autor": "Kiera Cass",
        "ano": 2012
    },
    {
        "id": 3,
        "titulo": "Tartarugas até lá embaixo",
        "autor": "John Green",
        "ano": 2017
    }
  ]
}
```

---

