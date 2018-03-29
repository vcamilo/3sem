import requests as req
from flask import jsonify

'''
coloque sua chave do omdb aqui.

Se voce nao criou ou nao lembra, pode pedir emprestado para um amigo
'''
 
chave_omdb='fd2ee97e'

'''
Crie uma funçao existe_id de busca no OMDB, 
que dada uma id, retorna se a id existe na base do omdb ou nao.

(ou seja, True se existe e false caso contrário)

Essa função, você pode testar no run_module.

Por exemplo

existe_id('nao') deve retornar False
existe_id('tt1211837') deve retornar True

lembrando: a URL em questao eh
url = "http://www.omdbapi.com/?apikey={}&i={}".format(chave_omdb, id_omdb)

para pegarmos o json, fazemos
retorno = req.get(url).json()
e retorno eh um dicionario

se nao estiver funcionando, use print(url) e verifique o que o omdb esta
te mandando

'''

def existe_id(id_omdb):
    url = "http://www.omdbapi.com/?apikey={}&i={}".format(chave_omdb, id_omdb)
    retorno = req.get(url).json()
    if "Error" in retorno:
        return False
    return True


'''Crie uma funcao pega_nome que, dada uma id do omdb, devolve o nome do filme

Ela é muito similar a funcao existe_id, so que acessa outra posicao do dicionario.

Alias, se a id nao existir, retorne 'id nao encontrada'
'''

def pega_nome(id_omdb):
    return 'id nao encontrada'

'''
relacionados, no formato
{
  'name': 'nome',
  'film_id': 'IMDB_id'
}
'''

