from flask import Flask,jsonify,abort
from flask import make_response, request, url_for


app = Flask(__name__)
professores = [
        {'nome':"joao", 'id_professor': 1},
        {'nome':"jose", 'id_professor': 2},
        {'nome':"maria", 'id_professor': 3}
        ]

alunos = [
        {'nome':"alexandre", 'id_aluno':10},
        {'nome':"miguel", 'id_aluno':20},
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
           return resposta

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
Crie uma URL /aluno_de_disciplina/<int:id_aluno>/<int:id_disciplina>

Ela deve retornar se um professor leciona ou nao uma determinada disciplina

Se ele leciona, o retorno deve ser
{'response':'True', 'aluno':'True'}

Caso contrario,
{'response':'True', 'aluno':'False'}

Se a disciplina nao for encontrada, retorne
{'response':'False', 'error':'disciplina nao encontrada'}

e o codigo de status 404
'''

@app.route('/aluno_de_disciplina/<int:id_aluno>/<int:id_disciplina>/', methods=['GET'])
def estuda(id_aluno,id_disciplina):
    for disciplina in disciplinas:
        if (id_disciplina == disciplina['id_disciplina']):
            if id_aluno in disciplina['alunos']:
                return jsonify({'response':'True', 'aluno':'True'})
            else:
                return jsonify({'response':'True', 'aluno':'False'})
    return jsonify({'response':'False', 'error':'disciplina nao encontrada'}),404

'''
(ja feito na aula passada)
Crie uma URL /leciona/<int:id_professor>/<int:id_disciplina>

Ela deve retornar se um professor leciona ou nao uma determinada disciplina

Se ele leciona, o retorno deve ser
{'response':'True', 'leciona':'True'}

Caso contrario,
{'response':'True', 'leciona':'False'}

Se a disciplina nao for encontrada, retorne
{'response':'False', 'error':'disciplina nao encontrada'}

e o codigo de status 404
'''

@app.route('/leciona/<int:id_professor>/<int:id_disciplina>/', methods=['GET'])
def leciona(id_professor,id_disciplina):
    for disciplina in disciplinas:
        if (id_disciplina == disciplina['id_disciplina']):
            if id_professor in disciplina['professores']:
                return jsonify({'response':'True', 'leciona':'True'})
            else:
                return jsonify({'response':'True', 'leciona':'False'})
    return jsonify({'response':'False', 'error':'disciplina nao encontrada'}),404

'''
Agora, vá para o arquivo acesso.py
'''

@app.route('/participantes/<int:id_disciplina>', methods=['GET'])
def participantes(id_disciplina):
        #lista todos ira armazenar todos os IDs envolvidos (prof/aluno)
        todos = []
        lista_nomes = []
        #iterando sob as disciplinas para localizar a disciplina localizada
        for disciplina in disciplinas:
                #disciplina localizada
                if id_disciplina == disciplina['id_disciplina']:
                        #adiciona IDs de alunos na lista todos
                        for aluno in disciplina['alunos']:
                                todos.append(aluno)
                        #adiciona IDs de professores na lista todos
                        for professor in disciplina['professores']:
                                todos.append(professor)
                        #compara o id da lista todos com o objeto professor e armazena o valor da chave 'nome' na lista_nomes
                        for professor in professores:
                                if professor['id_professor'] in todos:
                                        lista_nomes.append(professor['nome'])
                        #compara o id da lista todos com o objeto aluno e armazena o valor da chave 'nome' na lista_nomes
                        for aluno in alunos:
                                if aluno['id_aluno'] in todos:
                                        lista_nomes.append(aluno['nome'])
                                

                        
        print(lista_nomes)
        return jsonify({'participantes': lista_nomes})







if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')
