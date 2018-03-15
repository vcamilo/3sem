#!bin/python
from flask import Flask,jsonify,abort
from flask import make_response


app = Flask(__name__)

tasks_iniciais = [
    {
        'id': 1,
        'title': u'Fazer compras',
        'description': u'Leite, queijo, pizza, frutas',
        'done': False
    },
    {
        'id': 2,
        'title': u'Aprender flask',
        'description': u'http://flask.pocoo.org/docs/0.12/', 
        'done': False
    }
]

tasks = tasks_iniciais

'''
Você consegue abrir a pagina que geramos abaixo?

E os seus colegas?

Troque o texto
'''
@app.route('/')
def index():
        return "AEHOOOO!"
'''
A url definida nesse @app.route recebe a resposta da função;
Ou seja, acessando a URL veremos a resposta da função.

Nesse caso, a resposta é texto. A função "jsonify" transforma
objetos python em texto que representa json equivalente
'''
@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
     return jsonify(tasks)

'''
Note o uso do make_response, para retornar o codigo http 
para não encontrado e também um erro em formato json
'''
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    wanted_task = 'not found'
    for task in tasks: 
        if task['id'] == task_id:
            wanted_task = task
    if wanted_task == 'not found':
        return make_response(jsonify({'error': 'Task not found'}),
                             404)
    return jsonify({'task': wanted_task})

'''
Criar novas tarefas.

Veja que a URL é a mesma que a lista de tarefas.

O que muda é o  VERBO HTTP (lá era GET, aqui é POST)
'''
from flask import request
@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json:
        return make_response(jsonify({'error': 'Format not json'}),
                             400)
    '''um erro 400 indica um request mal formado'''
    task = {
        'id': tasks[-1]['id'] + 1,#temos um bom motivo para nao
#usar len(lista). Qual é?
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    '''201 é o codigo http para "recurso criado"'''
    return jsonify({'task': task}), 201
''' 
se quiser, de uma olhada em
https://en.wikipedia.org/wiki/List_of_HTTP_status_codes#2xx_Success
https://en.wikipedia.org/wiki/List_of_HTTP_status_codes#4xx_Client_errors
'''

''' crie uma função update que recebe um json parcial de uma 
tarefa, e altera apenas os elementos recebidos'''

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
        mudar = 'nao achei'
        for task in tasks:
                if task['id'] == task_id:
                        mudar = task
        if 'title' in request.json:
                mudar['title'] = request.json['title']
        if 'description' in request.json:
                mudar['description'] = request.json['description']
        if 'done' in request.json:
                mudar['done'] = request.json['done']
        return jsonify(mudar)


'''crie uma funcao delete_task, que deleta uma tarefa

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
  return 12

ela deve retornar erro se a tarefa não existir

'''
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
        for task in tasks:
                if task['id'] == task_id:
                        tasks.remove(0)
        return "Item deletado"


'''
Crie uma função de busca, que recebe uma string e retorna
todas as tarefas que contém essa string, ou no título
ou na descrição

@app.route('/todo/api/v1.0/tasks/search', methods=['GET'])
def search_text():
    #pega a query da url, se houver. Se nao, retorna None
    query = request.args.get('query',None)
    return 12
'''



'''
adicione um campo de prioridade às tarefas. Isso 
implica alterar a função de criação e a função de
update.

A prioridade deve ser um número em [0,1,2...,8,9]

Crie uma função que retorna a tarefa mais prioritária.
Se houver mais de uma, pode desempatar como quiser

(você também vai ter que alterar as tarefas iniciais e/ou
as chamadas do Postman)

@app.route('/todo/api/v1.0/tasks/highest', methods=['GET'])
def highest_priority():
  return 12

'''

'''
adicione as tarefas um novo campo que marca quando elas
foram criadas.

Esse campo deve ser preenchido pelo servidor quando a tarefa
é  recebida, nao enviado pelo cliente. Ele não
deve ser alterado se a tarefa for alterada.

Dica: pesquise python time objects

@app.route('/todo/api/v1.0/tasks/oldest', methods=['GET'])
def oldest():
    return 12
'''

'''
adicione um erro quando tentamos criar uma tarefa sem título.

Ele deve retornar um codigo adequado de erro E um erro 
auto-explicativo para o usuário, no formato json
'''

'''
Torne sua função de busca de tarefas com um determinado texto
"case-insentive". Ou seja, ela deve ignorar quais letras
são maiusculas ou minusculas quando ela faz a busca
'''

'''
DESAFIO:
Crie uma url que retorna as tarefas, ordenadas por prioridade.
'''


if __name__ == '__main__':
   app.run(debug=True, host='localhost')
