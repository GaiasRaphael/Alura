import csv
import json
from processamento_dados import Dados


def size_data (dados):
    return len (dados)

def join (dadosA, dadosB):
    combined_list = []
    combined_list.extend (dadosA)
    combined_list.extend (dadosB)
    return combined_list

def rename_columns (dados, keymapping):
    new_dados_csv = [{key_mapping.get (old_key): value for old_key, value in old_dict.items()} for old_dict in dados]
    return new_dados_csv

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

dados_empresaA = Dados (path_json, 'json')

dados_empresaB = Dados (path_csv, 'csv')

# Transformação de dados

key_mapping = {'Nome do Item' : 'Nome do Produto',
               'Classificação do Produto' : 'Categoria do Produto',
               'Quantidade em Estoque' : 'Quantidade em Estoque',
               'Nome da Loja' : 'Filial',
               'Valor em Reais (R$)' : 'Preço do Produto (R$)',
               'Data da Venda' : 'Data da Venda'}

dados_empresaB.rename_columns (key_mapping)
#print (dados_empresaB.nome_colunas)

dados_fusao = Dados.join (dados_empresaA, dados_empresaB)

# Load

path_dados_combinados = 'data_processed/dados_combinados.csv'
dados_fusao.salvando_dados (path_dados_combinados)
print (dados_fusao.path)