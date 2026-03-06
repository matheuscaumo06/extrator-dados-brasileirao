# ⚽ Pipeline ETL - Classificação do Brasileirão Série A

## 📖 Sobre o Projeto
Este projeto consiste em um pipeline simples de **Extração, Transformação e Carga (ETL)** de dados de futebol. O script conecta-se à API pública do [football-data.org](https://www.football-data.org/), extrai a tabela de classificação atualizada do Campeonato Brasileiro (Série A), realiza o tratamento dos dados estruturados em JSON e exporta o resultado final para um arquivo CSV pronto para análise.

O objetivo deste projeto é demonstrar fundamentos essenciais para a área de dados, incluindo o consumo de APIs REST com autenticação, manipulação de DataFrames e versionamento de código.

## 🛠️ Tecnologias Utilizadas
* **Python 3**
* **Bibliotecas:** `requests` (para extração via API) e `pandas` (para limpeza e transformação dos dados)
* **Gerenciamento de Ambiente:** `uv`
* **Versionamento:** Git e GitHub

## ⚙️ Como Executar o Projeto

### 1. Pré-requisitos
Certifique-se de ter o Python instalado na sua máquina. Recomenda-se o uso do `uv` para a criação rápida do ambiente virtual.

Você também precisará de uma Chave de API (API Key) gratuita, que pode ser gerada criando uma conta no site [football-data.org](https://www.football-data.org/).

### 2. Passo a Passo

Clone este repositório para a sua máquina local:
```bash
git clone [https://github.com/SEU_USUARIO/extrator-dados-brasileirao.git](https://github.com/SEU_USUARIO/extrator-dados-brasileirao.git)
cd extrator-dados-brasileirao