import requests 
import pandas as pd
import os 
from dotenv import load_dotenv

load_dotenv()

#minha API Key da footbal-data.org
api_key = os.getenv("API_KEY_FOOTBALL")

# URL
url = "https://api.football-data.org/v4/competitions/2013/standings"

headers = {
    "X-Auth-Token": api_key
}

print("Conectando à API do football-data.org")
resposta = requests.get(url, headers=headers)

#Verificação da conexão ( 200 = OK )
if resposta.status_code == 200:
    dados_json = resposta.json()
    tabela = dados_json['standings'][0]['table']
    df = pd.DataFrame(tabela)
    
    #Limpeza de dados
    df['nome_time'] = df['team'].apply(lambda x: x['name'])
    
    #Selecionando as colunas que importam
    colunas_selecionadas = ['position', 'nome_time', 'points','playedGames','won','draw','lost']
    df_limpo = df[colunas_selecionadas].copy()
    
    #Traduzindo os nomes das colunas
    df_limpo.columns = ['Posicao', 'Time', 'Pontos', 'Jogos', 'Vitorias', 'Empates', 'Derrotas']
    
    print("\n--- TABELA LIMPA ---")
    print (df_limpo.head())
    
    #Exportação dos Dados
    df_limpo.to_csv("classificacao_brasileirao.csv", index=False, encoding='utf-8')
    print("\nSucesso! Arquivo 'classificacao_brasileirao.csv' salvo.")
    
else:
    print(f"Erro: {resposta.status_code}")