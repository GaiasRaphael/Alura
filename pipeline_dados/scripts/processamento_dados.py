import csv 
import json

class Dados:

    def __init__(self, dados):
        self.dados = dados
        self.nome_colunas = self.__get_columns ()
        self.qtd_linhas = self.__size_data ()
        
    def __leitura_json (path):
        with open (path, 'r') as file:
            dados_json = json.load (file)
        return dados_json


    def __leitura_csv (path):
        dados_csv = []
        with open (path, 'r') as file:
            spamreader = csv.DictReader (file, delimiter=',')
            for row in spamreader:
                dados_csv.append(row)
        return dados_csv

    @classmethod
    def leitura_dados (cls, path, tipo_dados):
        dados = []

        if tipo_dados == 'csv':
            dados = cls.__leitura_csv (path)
        
        elif tipo_dados == 'json':
            dados = cls.__leitura_json (path)

        return cls(dados)

    def __get_columns (self):
        return list(self.dados[-1].keys ())

    def __size_data (self):
        return len (self.dados)

    def join (dadosA, dadosB):
        combined_list = []
        combined_list.extend (dadosA.dados)
        combined_list.extend (dadosB.dados)
        return Dados (combined_list)

    def rename_columns (self, key_mapping):
        new_dados_csv = [{key_mapping.get (old_key): value for old_key, value in old_dict.items()} for old_dict in self.dados]
        self.dados = new_dados_csv
        self.nome_colunas = self.__get_columns ()

    def __transformando_dados_tabela (self):
        dados_cobinados_tabela = [self.nome_colunas]

        for row in self.dados:
            linha = []
            for coluna in self.nome_colunas:
                linha.append (row.get (coluna, 'Indisponível'))
            dados_cobinados_tabela.append (linha)

        return dados_cobinados_tabela
    
    def salvando_dados (self, path):
        dados_combinados = self.__transformando_dados_tabela ()
        with open (path, 'w') as file:
            writer = csv.writer (file)
            writer.writerows(dados_combinados)
        