import requests
from math import ceil
import pandas as pd

class Dadosrepositorios:

    def __init__(self, owner):
        self.owner = owner
        self.api_base_url = 'https://api.github.com'
        self.access_token = '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'
        self.header = {'Authorization': f'token {self.access_token}', 
                        'X-Github-Api-Version': '2022-11-28'}
        
    def lista_repositorios (self):
        repos_list = []
        url = f'https://api.github.com/users/{self.owner}'
        response = requests.get (url)
        max_page = ceil ((response.json ()['public_repos']) / 30)

        for page_num in range (0, max_page):
            try:
                url = f'{self.api_base_url}/users/{self.owner}/repos?page={page_num}'
                response = requests.get(url, headers=self.header)
                repos_list.append (response.json ())
            except:
                repos_list.append (None)

        return repos_list
    
    def nomes_repos (self, repos_list):
        repo_names = []

        for page in repos_list:
            for repo in page:
                try:
                    repo_names.append (repo['name'])
                except:
                    pass

        return repo_names
    
    def nomes_linguagens (self, repos_list):
        repos_language = []

        for page in repos_list:
            for repo in page:
                repos_language.append (repo['language'])
        
        return repos_language

    def create_df_languages (self):
        repos = self.lista_repositorios ()

        data = pd.DataFrame ()
        data['Repository_name'] = self.nomes_repos (repos)
        data['Language'] = self.nomes_linguagens (repos)

        return data
    
    def save_df (self, df):
        df.to_csv (f'dados/{self.owner}_languages.csv')
    

amazon_rep = Dadosrepositorios ('amzn')
ling_mais_usadas_amzn = amazon_rep.create_df_languages ()
# print (ling_mais_usadas)

netflix_rep = Dadosrepositorios ('netflix')
ling_mais_usadas_netflix = netflix_rep.create_df_languages ()

spotify_rep = Dadosrepositorios ('spotify')
ling_mais_usadas_spotify = spotify_rep.create_df_languages ()

amazon_rep.save_df (ling_mais_usadas_amzn)
netflix_rep.save_df (ling_mais_usadas_netflix)
spotify_rep.save_df (ling_mais_usadas_spotify)