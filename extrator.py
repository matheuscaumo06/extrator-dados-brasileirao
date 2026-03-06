import requests 
import pandas as pd

#minha API Key da footbal-data.org
api_key = "8408fa9619224599b4f9607ac3cd0518"

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
    
    #transforma o JSON em uma tabela do Pandas
    df = pd.DataFrame(tabela)
    
    print("Dados extraídos!")
    print(df.head()) #Mostra as 5 primeiras linhas da tabela[
else:
    print(f"Erro: {resposta.status_code}")