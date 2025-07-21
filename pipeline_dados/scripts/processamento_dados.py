import csv 
import json

class Dados:

    def __init__(self, path, tipo):
        self.path = path
        self.tipo = tipo
        self.dados = self.__leitura_dados ()
        self.nome_colunas = self.__get_columns ()
        self.tam_linhas = self.__size_data ()
        
    def __leitura_json (self):
        with open (self.path, 'r') as file:
            dados_json = json.load (file)
        return dados_json


    def __leitura_csv (self):
        dados_csv = []
        with open (self.path, 'r') as file:
            spamreader = csv.DictReader (file, delimiter=',')
            for row in spamreader:
                dados_csv.append(row)
        return dados_csv


    def __leitura_dados (self):
        dados = []

        if self.tipo == 'csv':
            dados = self.__leitura_csv ()
        
        elif self.tipo == 'json':
            dados = self.__leitura_json ()
        
        elif self.tipo == 'list':
            dados = self.path
            self.path = 'lista em memória'

        return dados

    def __get_columns (self):
        return list(self.dados[-1].keys ())

    def __size_data (self):
        return len (self.dados)

    def join (dadosA, dadosB):
        combined_list = []
        combined_list.extend (dadosA.dados)
        combined_list.extend (dadosB.dados)
        return Dados (combined_list, 'list')

    def rename_columns (self, key_mapping):
        new_dados_csv = [{key_mapping.get (old_key): value for old_key, value in old_dict.items()} for old_dict in self.dados]
        self.dados = new_dados_csv
        self.nome_colunas = self.get_columns ()

    def transformando_dados_tabela (self):
        dados_cobinados_tabela = [self.nome_colunas]

        for row in self.dados:
            linha = []
            for coluna in self.nome_colunas:
                linha.append (row.get (coluna, 'Indisponível'))
            dados_cobinados_tabela.append (linha)

        return dados_cobinados_tabela
    
    def salvando_dados (self, path):
        dados_combinados = self.transformando_dados_tabela ()
        with open (path, 'w') as file:
            writer = csv.writer (file)
            writer.writerows(dados_combinados)
        