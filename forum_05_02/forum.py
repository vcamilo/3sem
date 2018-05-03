from flask import Flask,jsonify,abort
from flask import make_response, request, url_for
import acesso

app = Flask(__name__)

todo_forum = [
        {
            'disciplina':2,
            'textos': [
                [  {'usuario':20,'texto':'nao entendi nada sobre juros','id_msg':221},
                    {'usuario':3,'texto':'vamos falar mais sobre juros na aula que vem', 'id_msg':222}],
                [  {'usuario':20, 'texto':'como fazer para calcular o balanco...', 'id_msg':223},
                   {'usuario':20, 'texto':'ah, deixa quieto, ja entendi', 'id_msg':224}]
                 
                    ]
            },
        {
            'disciplina':1,
            'textos':[
                [  {'usuario':20,'texto':'voces entenderam o exercicio?','id_msg':225},
                    {'usuario':10,'texto':'sim, de boa. Te explico amanha', 'id_msg':227}],
                
                ]
            
        }
        ]

next_post = 228
        
'''
Você consegue abrir a pagina que geramos abaixo?

Troque o texto!
'''
@app.route('/')
def index():
        return "Sistema de conversas academicas"

'''
pra facilitar o debug
'''
@app.route('/forum/ver_tudo/', methods=['GET'])
def get_all():
     return jsonify(todo_forum)

@app.route('/forum/<int:id_disciplina>/')
def get_texts(id_disciplina):

    pessoa = request.args.get('professor','')+request.args.get('aluno','')
    if pessoa == '':
        return jsonify({'response':False,'textos':[]})
    pessoa = int(pessoa)
    if not acesso.leciona(pessoa,id_disciplina) and not acesso.eh_aluno(pessoa,id_disciplina):
        return jsonify({'response':False,'textos':[]})
    for di in todo_forum:
        if(di['disciplina'] == id_disciplina):
            return jsonify({'response':True,'textos':di['textos']})

'''
Agora, vamos definir uma URL /forum/responder/<msg:id>/,
para responder a uma mensagem.

Para cada disciplina temos uma lista de listas chamada textos
Cada listinha dentro de textos corresponde a uma conversa, e 
cada elemento da listinha, a uma mensagem.

A idéia é que devemos achar a mensagem a que estamos respondendo,
e colocar a resposta no fim da listinha correspondente.

O usuário que está enviando a mensagem virá como parametro
na "query string". 

Ou seja, teremos acessos como

/forum/responder/<msg:id>/?professor=2
ou
/forum/responder/<msg:id>/?aluno=20

Dai, verificaremos se o usuário pode postar naquela disciplina 
(consultando controle_pessoas) e, se puder, gravaremos sua msg.
e responderemos {'response': True, 'post_id': id_do_post_criado}
usando (e atualizando!) a variavel next_post

Se nao puder, responderemos apropriadamente {'response':False,
'error': erro_explicativo}
'''
@app.route('/forum/responder/<int:id_msg>/', methods=['POST'])
def responder(id_msg):
    professor = request.args.get('professor','')
    aluno = request.args.get('aluno','')
    mensagem = request.json.get('texto',None)
    for disc in todo_forum:
            print(disc)
            for forum in disc['textos']:
                    print('\n')
                    

            #forum['textos'][0].append({'usuario':20, 'texto':'this is ground control to major tom', 'id_msg':224})

    

    return jsonify(id_msg,professor, aluno, mensagem)

















if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0',port=5050)
