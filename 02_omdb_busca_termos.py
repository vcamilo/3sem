import requests as req

'''
1) Usando o postman descubra quantos items 
no total o omdb tem para a busca por termo 'star wars'
r:
2) Faça a mesma coisa, só para filmes (busca por termo de
'star wars', mas só filmes)
r:
3) Faça a mesma coisa, só para jogos (busca por termo de 
'star wars', mas só jogos)
r:
'''

'''
faça uma função busca_qtd_filmes que retorna quantos
filmes batem com uma determinada busca '''

api_key = 'fd2ee97e'

def busca_qtd_filmes(texto_buscar):
    url = "http://www.omdbapi.com/?apikey={}&s={}".format(api_key, texto_buscar)
    retorno = req.get(url).json()
    print(url)
    dadosFilme = {
        'totalResults':retorno['totalResults'],
    }
    return int(dadosFilme['totalResults'])

'''
faça uma função busca_qtd_jogos que retorna quantos
jogos batem com uma determinada busca '''
def busca_qtd_jogos(texto_buscar):
    url = "http://www.omdbapi.com/?apikey={}&s={}&type=game".format(api_key, texto_buscar)
    retorno = req.get(url).json()
    print(url)
    dadosFilme = {
        'totalResults':retorno['totalResults'],
    }
    return int(dadosFilme['totalResults'])
'''
faça uma função busca_filmes que, dada uma busca, retorna
os dez primeiros filmes que batem com a busca.

a sua resposta deve ser uma lista, cada filme representado por 
um dicionário. cada dicionario deve conter os campos
'nome' (valor Title da resposta) e 'ano' (valor Year da resposta)
'''
def busca_filmes(texto_buscar):
    url = "http://www.omdbapi.com/?apikey={}&s={}".format(api_key, texto_buscar)
    retorno = req.get(url).json()
    lista = []
    print(url)
    for filme in retorno['Search']:
        dic_novo = {}
        dic_novo['nome'] = filme['Title']
        dic_novo['ano'] = filme['Year']
        lista.append(dic_novo)
    return lista

'''
DESAFIO: faça uma função busca_filmes_grande que, 
dada uma busca, retorna
os VINTE primeiros filmes que batem com a busca.
'''

def busca_filmes_grande(texto_buscar):
    resposta = []
    return resposta


import unittest

class TestStringMethods(unittest.TestCase):
    
    def test_01_qdt_filmes(self):
        self.assertEqual(int(busca_qtd_filmes('star wars')), 288)
        self.assertEqual(int(busca_qtd_filmes('star trek')), 185)
        self.assertEqual(int(busca_qtd_filmes('menace')), 118)
        self.assertEqual(int(busca_qtd_filmes('future')), 946)
    
    def test_02_qdt_jogos(self):
        self.assertEqual(int(busca_qtd_jogos('star wars')), 96)
        self.assertEqual(int(busca_qtd_jogos('star trek')), 60)
        self.assertEqual(int(busca_qtd_jogos('menace')), 9)
        self.assertEqual(int(busca_qtd_jogos('future')), 38)
    
    def test_03_busca(self):
        resposta = busca_filmes('star wars')
        self.assertEqual(len(resposta),10)
        achei = False
        for filme in resposta:
            if int(filme['ano']) == 1977:
                achei = True
            if 'ano' not in filme:
                print(filme)
                self.fail('ano nao encontrado')
            if 'nome' not in filme:
                print(filme)
                self.fail('nome nao encontrado')
        if not achei:
            self.fail('filme "A New Hope" nao encontrado')
    
    def test_04_busca_grande(self):
        resposta = busca_filmes_grande('star wars')
        self.assertEqual(len(resposta),20)
        achei = False
        for filme in resposta:
            if int(filme['ano']) == 1977:
                achei = True
            if 'ano' not in filme:
                print(filme)
                self.fail('ano nao encontrado')
            if 'nome' not in filme:
                print(filme)
                self.fail('nome nao encontrado')
        if not achei:
            self.fail('filme "A New Hope" nao encontrado')

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

