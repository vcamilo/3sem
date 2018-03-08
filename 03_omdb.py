import requests as req 

'essa é a minha chave de acesso à API'
api_key = 'fd2ee97e'

'''essa é a mesma funçao do arquivo 01, mas agora vamos fazer alterações nela'''

def pega_filme_por_id(film_id):
  url = "http://www.omdbapi.com/?apikey={}&i={}".format(api_key, film_id)
  retorno = req.get(url).json()
  print(url)
  if retorno['Response']=='False':
    return "ID inválida"

  dadosFilme = {
          'film_id': film_id,
          'nome':retorno['Title'],
          'ano': retorno['Year'],
          'diretor': retorno['Director'],
          'genero': retorno['Genre'],
          'poster': retorno['Poster'],
          }
          
  return (dadosFilme)

'''
star_wars tem  a id tt0076759
tt0796366 é a id de star trek
tt1211837 é a id de doctor strange
naoexiste é uma id invalida'''

''' 1) um dos campos que o servidor retorna para nós tem
a url de um poster. adicionar campo poster nos dadosFilme
2) Quando usamos uma id que nao existe, temos um erro.
Nesse caso, a função deverá devolver a string 'id invalida'
ao invés do objeto do filme (verifique primeiro no postman
para ter uma idéia do que fazer!)
3) DESAFIO: O servidor nos retorna várias notas diferentes
adicionar campo nota_rotten_tomatoes nos dadosFilme
'''

import unittest

class TestStringMethods(unittest.TestCase):
    
    def test_01_poster(self):
        resposta = pega_filme_por_id('tt0796366')
        self.assertEqual(resposta['poster'],
        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjE5NDQ5OTE4Ml5BMl5BanBnXkFtZTcwOTE3NDIzMw@@._V1_SX300.jpg")
    
    def test_02_invalida(self):
        resposta = pega_filme_por_id('tt0796366naoao')
        self.assertEqual(resposta,'id invalida')
        resposta = pega_filme_por_id('bonde')
        self.assertEqual(resposta,'id invalida')
        resposta = pega_filme_por_id('blackkamenrider')
        self.assertEqual(resposta,'id invalida')
    
    def test_03_nota(self):
        resposta = pega_filme_por_id('tt0796366')
        self.assertEqual(resposta['nota_rotten_tomatoes'],
        "94%")


def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

