import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build

SCOPE = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
SPREADSHEET_NAME = 'Books Scraper'
CSV_FILE_NAME = 'books_data.csv'

creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', SCOPE)
gc = gspread.authorize(creds)

spreadsheet = gc.open(SPREADSHEET_NAME)
spreadsheet_id = spreadsheet.id

worksheet_analise_geral = spreadsheet.worksheet('Análise Geral')
worksheet_dist_preco = spreadsheet.worksheet('Distribuição de Preço')

df = pd.read_csv(CSV_FILE_NAME)

df['Price'] = df['Price'].str.replace('£', '').astype(float)

stats = [
    ['Preço Médio', f"£{df['Price'].mean():.2f}"],
    ['Preço Mínimo', f"£{df['Price'].min():.2f}"],
    ['Preço Máximo', f"£{df['Price'].max():.2f}"],
    ['Número Total de Livros', str(len(df))],
]

worksheet_analise_geral.clear()
worksheet_analise_geral.update('A1', [['Métrica', 'Valor']] + stats)

bins = [0, 10, 20, 30, 40, 50, 60, 1000]
labels = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60+']
df['Price Range'] = pd.cut(df['Price'], bins=bins, labels=labels, right=False)
price_dist = df['Price Range'].value_counts().sort_index()

worksheet_dist_preco.clear()
worksheet_dist_preco.update('A1', [['Faixa de Preço', 'Quantidade']] + price_dist.reset_index().values.tolist())

service = build('sheets', 'v4', credentials=creds)

requests = [{
    "addChart": {
        "chart": {
            "spec": {
                "title": "Distribuição de Preços",
                "pieChart": {
                    "legendPosition": "RIGHT_LEGEND",
                    "threeDimensional": False,
                    "domain": {
                        "sourceRange": {
                            "sources": [{
                                "sheetId": worksheet_dist_preco.id,
                                "startRowIndex": 0,
                                "endRowIndex": len(price_dist)+1,
                                "startColumnIndex": 0,
                                "endColumnIndex": 1
                            }]
                        }
                    },
                    "series": {
                        "sourceRange": {
                            "sources": [{
                                "sheetId": worksheet_dist_preco.id,
                                "startRowIndex": 0,
                                "endRowIndex": len(price_dist)+1,
                                "startColumnIndex": 1,
                                "endColumnIndex": 2
                            }]
                        }
                    }
                }
            },
            "position": {
                "overlayPosition": {
                    "anchorCell": {
                        "sheetId": worksheet_dist_preco.id,
                        "rowIndex": 0,
                        "columnIndex": 3
                    },
                    "offsetXPixels": 0,
                    "offsetYPixels": 0,
                    "widthPixels": 600,
                    "heightPixels": 400
                }
            }
        }
    }
}]

body = {'requests': requests}

response = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body=body).execute()

print("Análise atualizada com sucesso!")
