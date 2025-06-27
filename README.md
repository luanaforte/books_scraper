# 📚 Projeto de Web Scraping e Análise de Livros

Este projeto Python automatiza o processo de **raspagem de dados** de livros no site [Books to Scrape](https://books.toscrape.com), organiza os dados com **Pandas**, envia para uma **planilha no Google Sheets** e gera um **relatório de resumo e análise com gráficos**, demonstrando automação de coleta de dados e visualização.

---

## 🚀 Funcionalidades

- ✅ Raspagem de dados (título, link, preço e estoque) de 1000 livros
- ✅ Armazenamento local em CSV
- ✅ Upload automático para uma planilha do Google Sheets
- ✅ Geração de relatório estatístico em `.txt`
- ✅ Gráfico com distribuição de preços
---

## 📊 Acessar a Planilha

👉 [Clique aqui para visualizar os dados no Google Sheets](https://docs.google.com/spreadsheets/d/1wQ00UO4AQHDQbh2DX33eL3iAhWTUXIzDCPTN5YslD4o/edit?gid=0#gid=0)

---

## 🛠️ Tecnologias Utilizadas

| Ferramenta         | Finalidade                                                                 |
|--------------------|---------------------------------------------------------------------------|
| `requests`         | Faz as requisições HTTP para obter o conteúdo das páginas                 |
| `beautifulsoup4`   | Faz o parsing do HTML para extrair dados específicos                      |
| `pandas`           | Estrutura, limpa, analisa e exporta os dados em CSV                       |
| `gspread`          | Conecta e atualiza planilhas do Google Sheets via Python                  |
| `oauth2client`     | Autenticação com credenciais da API do Google                             |
| `googleapiclient`  | Cria gráficos na planilha diretamente pela API do Google                  |
| `datetime`         | Gera o timestamp no relatório de resumo                                   |

---

## 📁 Estrutura de Pastas

```

RAIZ/
├── src/
│ ├── web_scraping.py # Raspagem do site
│ ├── upload_to_sheets.py # Envia para Google Sheets
│ ├── generate_analysis.py # Gera relatório com estatísticas
├── books_data.csv # Dados coletados
├── credentials.json # Sua chave de API do Google (deve estar no .gitignore)
├── .gitignore

```

---

## ⚙️ Como usar na sua máquina

### 1. Instale as bibliotecas

```bash
pip install requests beautifulsoup4 pandas gspread oauth2client google-api-python-client
```

### 2. Configure a API do Google Sheets

1.  Vá ao [Google Cloud Console](https://console.cloud.google.com/).
2.  Crie um projeto (ou selecione um existente).
3.  Ative as seguintes APIs no projeto:
    * ✅ **Google Sheets API**
    * ✅ **Google Drive API**
4.  Crie uma conta de serviço:
    * No Cloud Console, navegue até **"IAM e Admin" > "Contas de serviço"**.
    * Siga as instruções para criar uma nova conta de serviço, concedendo a ela um papel apropriado (ex: "Editor" ou "Editor de planilhas").
    * Após a criação, baixe a chave da conta de serviço como um arquivo **`.json`**.
    * **Renomeie este arquivo para `credentials.json`**.
5.  Compartilhe sua planilha do Google Sheets com o e-mail da conta de serviço. Este e-mail pode ser encontrado no arquivo `credentials.json` e termina com `@<seu-projeto>.iam.gserviceaccount.com`. Certifique-se de conceder permissão de **"Editor"**.

---

### ▶️ Ordem de Execução dos Scripts

Os scripts devem ser executados em uma sequência específica. **Sempre execute os comandos a partir da pasta raiz do seu projeto**:

1.  **Raspar os dados:**
    ```bash
    python src/web_scraping.py
    ```
2.  **Enviar para o Google Sheets:**
    ```bash
    python src/upload_to_sheets.py
    ```
3.  **Realizar a Análise e Gerar Gráficos na Planilha:**
    ```bash
    python src/generate_analysis.py
    ```
