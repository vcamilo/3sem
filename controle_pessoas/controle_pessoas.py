from flask import Flask,jsonify,abort
from flask import make_response, request, url_for


app = Flask(__name__)
professores = [
        {'nome':"joao", 'id_professor': 1},
        {'nome':"jose", 'id_professor': 2},
        {'nome':"maria", 'id_professor': 3}
        ]

alunos = [
        {'nome':"alexandre", 'id_aluno':1},
        {'nome':"miguel", 'id_aluno':2},
        {'nome':"paulo", 'id_aluno':3},
        {'nome':"pedro", 'id_aluno':4},
        {'nome':"henrique", 'id_aluno':5},
        {'nome':"mauro", 'id_aluno':6},
        {'nome':"arthur", 'id_aluno':7},
        ]

disciplinas = [
        {'nome':"distribuidos", 'id_disciplina':1, 'alunos':[1,2], 'professores':[1], 'publica': 'False'},
        {'nome':"matematica financeira", 'id_disciplina':2, 'alunos':[2], 'professores':[3], 'publica': 'True'},
        {'nome':"matematica basica", 'id_disciplina':3, 'alunos':[1,2], 'professores':[3,2], 'publica': 'False'}
        
        ]


'''
Você consegue abrir a pagina que geramos abaixo?

Troque o texto!
'''
@app.route('/')
def index():
        return "Sistema de controle de pessoas"

'''
Vou deixar a primeira URL definida, pra facilitar o debug
'''
@app.route('/pessoas/ver_tudo/', methods=['GET'])
def get_all():
     return jsonify([professores,alunos,disciplinas])

'''
Vamos fazer dois exemplos de URLs. Duas versoes da URL /professor/<int:professor_id> 
para vermos os dados de um professor.

Com isso, veremos como implementar as boas praticas recomendadas na aula passada
'''
@app.route('/nao_encapsulada/professor/<int:id_professor>', methods=['GET'])
def get_professor(id_professor):
    for professor in professores:
        if professor['id_professor'] == id_professor:
           copia = dict(professor) #é importante copiarmos o dicionario, como fizemos aqui.
           #se tivessemos feito copia = professor, teriamos duas variaveis apontando
           #para o mesmo objeto, de forma que ao adicionar a url em copia,
           #adicionariamos tambem na variavel professor
           copia['url'] = url_for('get_professor',id_professor=copia['id_professor'])
           #note a funcao url_for. Ela recebe uma string, que é um nome de funcao,
           # e as variaveis, na forma  nome_variavel = valor_da_variavel;
           #Se quisessemos a url para o professor 200, fariamos
           # url_for('get_professor',id_professor=200)
           resposta = jsonify(copia)
           return make_response(resposta, 200)

'''
Segunda versao da URL /professor/<int:professor_id> 
'''
@app.route('/professor/<int:id_professor>', methods=['GET'])
def get_professor_completa(id_professor):
    for professor in professores:
        if professor['id_professor'] == id_professor:
           copia = dict(professor)
           copia['url'] = url_for('get_professor_completa',id_professor=copia['id_professor'])
           resposta = jsonify({'response':'True','professor':copia})
           #agora a resposta tem um formato padrao, tanto para erro quanto para correto.
           #é um dicionario que sempre contem o campo response.
           return resposta
    #e estamos devolvendo um erro quando ele ocorre
    resposta = jsonify({'response':'False','error':'id de professor inválida'})
    return resposta,404


'''
Crie uma URL que adiciona um professor,
fazendo POST na URL /professores/

Retorne o objeto criado.

Nao esqueca de adicionar a URL no objeto retornado,
mas nao no criado.

Nao esqueca de "encapsular" o objeto retornado,
retornando:
{'response':"True","professor":(objeto do professor)}
No caso de dar tudo certo, o codigo http a retornar é 201 (created)

Se o professor vier sem nome no request ou com a string vazia,
dê um erro 400, retornando jsonify({'response':'False','error':'nome nao enviado'}),400
'''
@app.route('/professores/', methods=['POST'])
def create_professor():
    '''201 é o codigo http para "recurso criado"'''
    print(request.json)
    if request.json == {}:
            return make_response(jsonify({'Error': 'nome nao enviado', 'Response': False}),400)
    if request.json['nome'] == "":
            return make_response(jsonify({'Error': 'corpo mal formado', 'Response': False}),400)
 
    professor = {
            'nome': request.json['nome'],
            'id_professor': professores[-1]['id_professor'] + 1
            }
    professores.append(professor)
    retorno = dict(professor)
    retorno.pop('id_professor', None)
    retorno['url'] = url_for('create_professor')
    retorno['url'] += str(professor['id_professor'])

    return make_response(jsonify({'professor': retorno, 'response': True}), 201)

'''
Façamos agora a consulta de aluno por ID, nos mesmos moldes da consulta do professor

Atenção ao encapsulamento da resposta, 
e nao esqueca de adicionar a URL na resposta sem afetar 
o objeto armazenado
'''
@app.route('/aluno/<int:id_aluno>', methods=['GET'])
def get_aluno_completa(id_aluno):
        for aluno in alunos:
                if aluno['id_aluno'] == id_aluno:
                        retorno = {
                                'nome': aluno['nome'],
                                'url': url_for('get_aluno_completa',id_aluno=aluno['id_aluno'])
                                }
                        return make_response(jsonify({'aluno': retorno, 'response': True}), 200)
        return make_response(jsonify({'erro': 'aluno não encontrado', 'response': False}), 400)

'''
Façamos agora a consulta de disciplina por ID, nos mesmos moldes da consulta do professor

Atenção ao encapsulamento da resposta, 
e nao esqueca de adicionar a URL na resposta sem afetar 
o objeto armazenado

{'nome':"distribuidos", 'id_disciplina':1, 'alunos':[1,2], 'professores':[1], 'publica': 'False'},

'''
@app.route('/disciplina/<int:id_disciplina>', methods=['GET'])
def get_disciplina_completa(id_disciplina):
        for disciplina in disciplinas:
                if disciplina['id_disciplina'] == id_disciplina:
                        retorno = {
                                'nome': disciplina['nome'],
                                'url': url_for('get_disciplina_completa', id_disciplina=disciplina['id_disciplina']),
                                'alunos': disciplina['alunos'],
                                'professores': disciplina['professores'],
                                'publiaa': disciplina['publica']
                                }
                        return make_response(jsonify({'disciplina': retorno, 'response': True}), 200)
        return make_response(jsonify({'erro': 'disciplina não encontrada', 'response': False}), 400)

'''
Façamos agora uma consulta de disciplina por nome, recebendo 
o parametro de busca como uma query string na URL.

Queremos usar a URL /disciplina/busca/
Um exemplo de acesso seria /disciplina/busca/?busca=matematica

Para acessar a query string, temos o dicionario request.args.
Ou seja, a busca da URL acima pode ser acessada por
request.args['busca'] ou request.args.get('busca')

O resultado deve ser uma lista de disciplinas cujo nome "bate" com a busca

Lembre-se se encapsular a resposta e de retornar a url da disciplina

Retorne um erro se o usuario nao forneceu o termo de busca.

Se deu tudo certo, a resposta deve ser da forma:
    
    {'response':'True','disciplinas':lista_das_disciplinas_com_respectivas_URLs}
'''
@app.route('/disciplina/busca/', methods=['GET'])
def get_disciplina_busca():
        busca = request.args.get('busca')
        disc = []
        if busca == None or busca == "":
                return make_response(jsonify({'bad request': 'insira o campo de busca'}), 400)
        for disciplina in disciplinas:
                if disciplina['nome'].find(busca) != -1:
                        disc.append(disciplina)                        
        if disc == []:
                return make_response(jsonify({'busca': 'sua busca não obteve resultados', 'response': False}), 200)
        retorno = list(disc)
        for materias in retorno:
                retorno[0]['url'] = url_for('get_disciplina_busca')
                retorno[0]['url'] += str(disc[0]['id_disciplina'])
                retorno[0].pop('id_disciplina', None)
        
        #corrige isso
        
        return make_response(jsonify({'busca':retorno, 'response': True}), 200)
        

'''
A proxima funcao nao tem runtests implementado :(

Agora, façamos uma funcao que adiciona um aluno a uma disciplina
na url  '/disciplina/<int:id_disciplina>/adiciona_aluno' com o metodo PUT

No body, ela recebe {'id_aluno':(uma id valida)}

Ela deve retornar erro 404 se o aluno nao existe

Ela deve nao adicionar um aluno mais de uma vez (teste via POSTMAN!)

'''
@app.route('/disciplina/<int:id_disciplina>/adiciona_aluno', methods=['PUT'])
def add_aluno(id_disciplina):
    return str(request.json['id_aluno'])





if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')
