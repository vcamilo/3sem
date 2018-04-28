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

'''
Vamos implementar a funcao de visualizacao do forum:

    Ao acessar /forum/2/, devemos receber as mensagens para a disciplina 2.
    Isso só deve ocorrer, porém, se temos autorizacao para ver essas mensagens,
    Para isso, usaremos os parametros de query "professor" ou "aluno".

    Por exemplo, ao acessar /forum/2/?professor=3,
    devemos retornar um dicionario, com dois campos:
      response=True
      campo textos contendo uma lista de todos os textos daquela disciplina (o objeto textos
        daquela disciplina inteiro)

    O mesmo deve acontecer se acessarmos /forum/2/?aluno=20

    Ja se acessarmos apenas /forum/2/, devemos receber um dicionario com os mesmos dois campos
      response=False
      campo textos contendo uma lista vazia

    A mesma lista vazia deve ser retornada caso o aluno ou professor nao faca parte da 
    disciplina
'''
@app.route('/forum/<int:id_disciplina>/')
def get_texts(id_disciplina):
    professor = request.args.get('professor','')
    aluno = request.args.get('aluno', '')
    copia = []
    print()
    if aluno == '' and professor == '':
            return jsonify({'response': False, 'textos':[]})
    for forum in todo_forum:
            if id_disciplina == forum['disciplina']:
                    if professor != '':
                            if(acesso.leciona(professor, id_disciplina)):
                                    #copia.append(forum['textos'])
                                    print(forum['textos'][0][0]['texto'])
                                    return jsonify({'textos':forum['textos'], 'response': True})
                            else:
                                    return jsonify({'response': False, 'textos':[]})
                    elif aluno != '':
                            print(aluno)
                            if(acesso.eh_aluno(aluno, id_disciplina)):
                                    copia.append(forum['textos'])
                                    return jsonify({'textos':forum['textos'], 'response': True})
                            else:
                                    return jsonify({'response': False, 'textos':[]})
    return jsonify({'response': False, 'error': 'disciplina nao encontrada'})
                    


'''
Agora, adicione na leitura do forum um novo campo.

Além de "response" e "textos", ele deve incluir um campo "participantes".
Esse campo é uma lista de strings, onde cada string é o
**nome** de um participante (aluno ou professor)
daquele forum

Para isso, voce terá que criar uma nova URL em controle pessoas, para
obter o nome dos envolvidos na disciplina

Depois, uma funcao no arquivo acesso.py para acessar essa URL

E depois, alterar a funcao acima.
'''

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0',port=5050)
