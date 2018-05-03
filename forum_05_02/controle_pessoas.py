from flask import Flask,jsonify,abort
from flask import make_response, request, url_for


app = Flask(__name__)
professores = [
        {'nome':"joao", 'id_professor': 1, 'email': 'joao@example.com'},
        {'nome':"jose", 'id_professor': 2, 'email': 'jose@example.com'},
        {'nome':"maria", 'id_professor': 3, 'email': 'maria@example.com'}
        ]

alunos = [
        {'nome':"alexandre", 'id_aluno':10, 'email':'alex@example.com'},
        {'nome':"miguel", 'id_aluno':20, 'email':'miguel@example.com'},
        ]

disciplinas = [
        {'nome':"distribuidos", 'id_disciplina':1, 'alunos':[10,20], 'professores':[1], 'publica': 'False'},
        {'nome':"matematica financeira", 'id_disciplina':2, 'alunos':[20], 'professores':[3], 'publica': 'True'},
        {'nome':"matematica basica", 'id_disciplina':3, 'alunos':[10], 'professores':[3,2], 'publica': 'False'}
        
        ]

'''
Você consegue abrir a pagina que geramos abaixo?

Troque o texto!
'''
@app.route('/')
def index():
        return "Sistema de controle de pessoas"

'''
pra facilitar o debug
'''
@app.route('/pessoas/ver_tudo/', methods=['GET'])
def get_all():
     return jsonify([professores,alunos,disciplinas])

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
           return resposta

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

@app.route('/leciona/<int:id_professor>/<int:id_disciplina>/', methods=['GET'])
def leciona(id_professor,id_disciplina):
    for disciplina in disciplinas:
        if (id_disciplina == disciplina['id_disciplina']):
            if id_professor in disciplina['professores']:
                return jsonify({'response':'True', 'leciona':'True'})
            else:
                return jsonify({'response':'True', 'leciona':'False'})
    return jsonify({'response':'False', 'error':'disciplina nao encontrada'}),404


@app.route('/aluno_de_disciplina/<int:id_aluno>/<int:id_disciplina>/', methods=['GET'])
def estuda(id_aluno,id_disciplina):
    for disciplina in disciplinas:
        if (id_disciplina == disciplina['id_disciplina']):
            print(disciplina, 'procurando', id_aluno)
            if id_aluno in disciplina['alunos']:
                print(id_disciplina,disciplina['alunos'])
                return jsonify({'response':'True', 'aluno':'True'})
            else:
                return jsonify({'response':'True', 'aluno':'False'})
    return jsonify({'response':'False', 'error':'disciplina nao encontrada'}),404

'''
Implemente uma funcao que recebe uma lista de ids de usuários (podem
ser professores ou alunos) e retorne a lista de emails correspondentes

Se der tudo certo, a resposta deve ser da forma {response:True, emails:['a@gmail.com','b@yahoo.com']}

Se der algo errado, a resposta deve ser da forma {response:False, error: 'descricao do erro'}

Um erro possivel é o usuário enviar uma id inexistente: nesse caso, é conveniente retornar o codigo http 404
junto com o json
'''

@app.route('/emails/', methods=['GET'])
def emails():
    string_ids = request.args.get('lista_ids','')
    lista_ids = string_ids.split(',')
    emails = []
    for professor in professores:
        for item in lista_ids:
            if int(item) == professor['id_professor']:
                emails.append(professor['email'])
    for aluno in alunos:
        for item in lista_ids:
            if int(item) == aluno['id_aluno']:
                emails.append(aluno['email'])
    if emails == []:
        return jsonify({'response':False, 'error': 'nao ha nenhum aluno/professor com a(s) ID(s) informadas'})
    return jsonify({'E-mails': emails})


if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')
