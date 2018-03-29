import requests as req 

'essa é a minha chave de acesso à API'
api_key = '29a71837'


def pega_filme_por_id(film_id):
  url = "http://www.omdbapi.com/?apikey={}&i={}".format(api_key, film_id)
  retorno = req.get(url).json()
  print(url)

  dadosFilme = {
          'film_id': film_id,
          'nome':retorno['Title'],
          'ano': retorno['Year'],
          'diretor': retorno['Director'],
          'genero': retorno['Genre'],
          }
          
  return (dadosFilme)

star_wars = pega_filme_por_id('tt0076759')
'''vamos experimentar essa função.
rode a função com as seguintes buscas:
tt0796366 é a id de star trek
tt1211837 é a id de doctor strange
naoexiste é uma id invalida'''


