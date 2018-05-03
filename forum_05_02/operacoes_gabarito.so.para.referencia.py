from flask import Flask,jsonify,abort
from flask import make_response, request


app = Flask(__name__)

@app.route('/')
def index():
        return "Funcoes matematicas!"

'''
defina uma url potencia de 2, de forma que 
chamar /matematica/potencia_de_dois/<int:expoente>
com o metodo GET calcule a potencia desejada.

Por exemplo, ao acessarmos 
http://localhost:5000/matematica/potencia_de_dois/5
devemos receber 
{ "resposta": 32 }
'''

@app.route('/matematica/potencia_de_dois/<int:pot>', methods=['GET'])
def calc_pot(pot):
        res = 2 ** pot
        return jsonify({'resposta': res})
'''
Note: a regra acima, definida no app.route, associa URLs do tipo /matematica/potencia_de_dois/3
a uma funcao calc_pot.

A sintaxe <int:pot> indica um lugar na url onde aparecerá um inteiro, e esse inteiro
é associado a uma variavel pot (que a funcao cal_pot recebe)

A função retorna texto puro: jsonify({'resposta': res}) retorna uma string
que é a representacao do dicionario {'resposta': 8} (ou qual for o valor de res)
na linguagem json (que estamos usando desde a aula passada, talvez sem perceber.
O OMDB retornava json, e o python interpretava pra gente e montava dicionários e listas)

Isso é importante: a funcao deve retornar texto, se voce tentasse retornar o dicionario
{'resposta':res} ao inves de jsonify({...}), possivelmente teria problemas
'''

'''
Quando não mandarmos o numero, retorne 
{'erro':'sem expoente'} e o codigo de erro 400
'''


@app.route('/matematica/potencia_de_dois/', methods=['GET'])
def erro_pot():        
        return jsonify({'erro': 'Sem expoente'}), 400

'''
Duas coisas para ver aqui: definimos uma segunda URL para tratar o erro.

Isso porque, quando temos /matematica/potencia_de_dois/12, automaticamente
temos um "match" com a funcao lah de cima (calc_pot).

Quanto temos /matematica/potencia_de_dois/, esse match nao ocorre.
Em vez disso, ele vai ocorrer com essa nossa funcao erro_pot

Outra coisa: perceba que retornamos duas coisas: um texto (o jsonify) e um numero
O numero eh um codigo de status HTTP. Ao irmos no postman, poderemos ver que 
ele significa "bad request".

Quando ocorre um erro, é importante retornar tanto um código HTTP adequado
quanto um texto para o programador do outro lado poder ler e ter uma 
ideia do que está acontecendo
'''

'''
Para a URL /matematica/soma, com o método POST,
queremos o seguinte:

Que ela receba um json no corpo (body) do request,
e esse json deve definir dois numeros (a e b)

Ela deve retornar um json {resposta: v} onde v=a+b

Se o json nao contiver as chaves a ou b, ela deve retornar
um erro 400 (request mal formado) e um texto de erro
'''
@app.route('/matematica/soma', methods=['POST'])
def calc_soma():
        if 'a' not in request.json or 'b' not in request.json:
                return jsonify({'error': 'parametro "a" ou parametro "b" nao recebidos'}), 400
        soma = request.json['a']+request.json['b']
        return jsonify({'resposta': soma})

'''
A coisa principal que vemos aqui é o jeito de acessar dados passados no corpo do 
request: através do dicionário request.json

Outra coisa importante: essa URL está aceitando o verbo HTTP POST, nao o GET, 
(compare com as duas funcoes anteriores). Requests do tipo GET nao contem corpo.
'''

'''
Crie a mesma função soma, agora recebendo os parametros 
através da URL

Ou seja,

http://localhost:5000/matematica/soma?b=13&a=12

Deverá retornar

{
    "soma": 25
}

(esses parametros estao sendo mandados na URL de uma forma
padrao, e o flask dá suporte a isso.
Nao deixe de rodar o soma get e o soma get invertido
no postman)
'''
@app.route('/matematica/soma', methods=['GET'])
def soma_url():
        valorA = request.args.get('a', '')
        valorB = request.args.get('b', '')
        return jsonify({"soma": valorA + valorB})

'''
Aqui estamos vendo uma segunda maneira de mandar dados para o servidor 
através da URL que acessamos: alem do "caminho", que estamos usando
para definir qual funcao rodar, temos tambem a "query string", varios 
pares do tipo chave-> valor que o flask disponibiliza para gente
no dicionario request.args
'''

'''
Usamos 4 construcoes interessantes sobre dicionarios hoje:

   verificamos se uma chave está em um dicionario, fazendo chave in dic (linha 85)
   acessamos dicionarios com dici['chave'] (linha 87)
   definimos dicionarios, como {"soma": valorA + valorB} (linha 121)
   e acessamos tambem com dici.get('chave','resposta padrao') (linha 119)
      esse ultimo é um truque para acessar dicionarios, se nao temos certeza
      se veio a chave. se a chave nao estiver no dicionario, recebemos a resposta
      padrao. Por exemplo dici={'a':12}; dici.get('a',100) resulta 12, porque a 
      chave 'a' está no dicionario, e dici.get('b',100) resulta 100, porque
      a chave 'b' nao esta

'''


'''
A partir daqui nao tem mais nada pra fazer
'''
if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')
