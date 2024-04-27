import pandas as pd
import json
import sqlalchemy
from sqlalchemy import create_engine, inspect, MetaData, Table

# Carregando as configurações do arquivo JSON
with open('configs.json') as config_file:
    config = json.load(config_file)

# Obtendo informações do Json de configuração
database_vendor = config['databaseVendor']['vendor']
database_oracle = config['databaseVendor']['origin']
database_ms = config['databaseVendor']['originMS']
tab_func = config['tableFunc']['nameTable']
parquet_file_path = config['fileFunc']['nameFile']

# Carregue os dados do arquivo Parquet em um DataFrame Pandas
df_parquet = pd.read_parquet(parquet_file_path)

if database_vendor == 'oracle':
    # Crie uma conexão com o banco de dados Oracle
    engine = sqlalchemy.create_engine(database_oracle)
else:
    # Crie uma conexão com o banco de dados MySQL
    engine = sqlalchemy.create_engine(database_ms)

# Crie um objeto MetaData
metadata = MetaData()

# Carregue as tabelas existentes do banco de dados
metadata.reflect(bind=engine)

if tab_func in metadata.tables:
    # Obtenha a tabela do banco de dados
    tabela = Table(tab_func, metadata, autoload=True, autoload_with=engine)
    
    # Drop a tabela
    tabela.drop(engine)
    print(f"A tabela '{tab_func}' foi dropada com sucesso.")
else:
    print(f"A tabela '{tab_func}' não existe no banco de dados. A mesma será criada")

# Use o Pandas para carregar os dados do DataFrame para a tabela do banco de dados
# Certifique-se de substituir 'if_exists' com 'replace' ou 'append' dependendo da sua necessidade
# Se quiser substituir a tabela existente, use 'replace', se quiser adicionar aos dados existentes, use 'append'
# df_parquet.to_sql(tab_func, engine, if_exists='replace', index=False)
df_parquet.to_sql(tab_func, engine, index=False)

print("Dados carregados com sucesso na tabela:", tab_func)
