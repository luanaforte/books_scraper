import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
spreadsheet_name = "Books Scraper" 
csv_file_name = "books_data.csv" 

print(f"Tentando enviar dados de '{csv_file_name}' para o Google Sheets...")

try:
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    print("Autorização do Google Sheets bem-sucedida.")
except Exception as e:
    print(f"Erro ao carregar credenciais ou autorizar gspread: {e}")
    print("Por favor, verifique se seu arquivo 'credentials.json' está correto e não está vazio.")
    exit()

try:
    spreadsheet = client.open(spreadsheet_name)
    print(f"Planilha '{spreadsheet_name}' aberta com sucesso.")
except gspread.exceptions.SpreadsheetNotFound:
    print(f"Erro: Planilha '{spreadsheet_name}' não encontrada.")
    print("Por favor, verifique se o nome da planilha está EXATO e se a conta de serviço tem acesso a ela.")
    exit()
except Exception as e:
    print(f"Ocorreu um erro ao abrir a planilha: {e}")
    exit()

sheet = spreadsheet.sheet1
print("Primeira aba da planilha selecionada.")

try:
    df = pd.read_csv(csv_file_name)
    print(f"Dados lidos de '{csv_file_name}' com sucesso.")
except FileNotFoundError:
    print(f"Erro: O arquivo '{csv_file_name}' não foi encontrado. Certifique-se de que o script de scraping foi executado e salvou o arquivo.")
    exit()
except Exception as e:
    print(f"Erro ao ler '{csv_file_name}': {e}")
    exit()

data_to_upload = [df.columns.values.tolist()] + df.values.tolist()

try:
    sheet.clear()
    print("Conteúdo da aba limpo (opcional).")
except Exception as e:
    print(f"Erro ao limpar a aba: {e}")
    
try:
    sheet.update('A1', data_to_upload)
    print("Dados enviados para o Google Sheets com sucesso!")
except Exception as e:
    print(f"Erro ao enviar dados para o Google Sheets: {e}")