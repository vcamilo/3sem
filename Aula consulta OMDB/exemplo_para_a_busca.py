import requests as req 

'essa é a minha chave de acesso à API'
api_key = 'fd2ee97e'


def pega_filme_por_nome(film_term):
  url = 'http://www.omdbapi.com/?apikey={}&s={}'.format(api_key, film_term)
  filmes = []
  retorno = req.get(url).json()

  for filme in retorno['Search']:
    filmes.append({
      'Titulo': filme['Title'],
      'Ano': filme['Year']
      });
##  dadosFilme = {
##          'film_id': retorno['imdbID'],
##          'nome':retorno['Title'],
##          'ano': retorno['Year'],
##          'diretor': retorno['Director'],
##          'genero': retorno['Genre'],
##          }
          
  return filmes

#star_wars = pega_filme_por_id('tt0076759')
'''vamos experimentar essa função.
rode a função com as seguintes buscas:
tt0796366 é a id de star trek
tt1211837 é a id de doctor strange
naoexiste é uma id invalida'''


