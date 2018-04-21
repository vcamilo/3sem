from flask import Flask,jsonify,abort
from flask import make_response, request, url_for
import acesso

app = Flask(__name__)
atividades = [
        {
            'id_atividade':1,
            'id_disciplina':1,
            'enunciado': 'crie um app de todo em flask',
            'respostas': [
                {'id_aluno': 1, 'resposta':'todo.py', 'nota':9},
                {'id_aluno': 2, 'resposta':'todo.zip.rar'}
                ]
        },

        {
            'id_atividade':2,
            'id_disciplina':1,
            'enunciado': 'crie um servidor que envia email em Flask',
            'respostas': []
        },

        ]

'''
Você consegue abrir a pagina que geramos abaixo?

Troque o texto!
'''
@app.route('/')
def index():
        return "Sistema de entrega de atividades"
'''
Vou deixar a primeira URL definida, pra facilitar o debug.
Nao mude ela em nada
'''
@app.route('/atividades/ver_tudo/', methods=['GET'])
def get_all():
     return jsonify(atividades)

'''
Crie uma URL para exibir uma atividade,
em /atividade/<int:id_atividade>

Ela deve retornar 
{'response': 'True', 'atividade': atividade_com_o_campo_extra_URL}
Se a atividade existir

E
{'response': 'False', 'erro': 'atividade nao encontrada'} com codigo de status 404 caso contrario

Cuidado para nao alternar a atividade 'no banco'!
'''
##@app.route('/atividade/<int:id_atividade>/')
##def atividade(id_atividade):
##        for atividade in atividades:
##                if id_atividade == atividade['id_atividade']:
##                        retorno = dict(atividade)
##                        retorno['url'] = url_for('atividade', id_atividade=retorno['id_atividade'])
##                        return make_response(jsonify({'response': 'True', 'atividade': retorno}), 200)
##                return make_response(jsonify({'response': 'False', 'erro': 'atividade nao encontrada'}), 400)

'''
Agora, vamos alterar o comportamento da URL anterior.

Ela deve receber como parametro de query uma id_professor.
Ela só deve retornar as respostas dos alunos se o professor
for um professor da disciplina. Caso contrario, deve suprimir
as respostas
'''

#O código acima foi comentado e reformulado abaixo

@app.route('/atividade/<int:id_atividade>/')
def atividade(id_atividade):
        id_professor = request.args.get('id_professor')
        for atividade in atividades:
                if id_atividade == atividade['id_atividade']:
                        try:
                                retorno_leciona = acesso.leciona(id_professor, atividade['id_disciplina'])
                                if retorno_leciona['response'] == False:
                                        return jsonify({'erro': 'ID de professor inválido', 'response': False})
                                if retorno_leciona['leciona']:
                                        retorno = dict(atividade)
                                        retorno['url'] = url_for('atividade', id_atividade=retorno['id_atividade'])
                                        return make_response(jsonify({'response': True, 'atividade': retorno}), 200)
                                else:
                                        retorno = dict(atividade)
                                        del retorno['respostas']
                                        retorno['url'] = url_for('atividade', id_atividade=retorno['id_atividade'])
                                        return jsonify({'response': True, 'atividade': retorno}), 200
                        except:
                                return jsonify({'error': 'erro interno do servidor', 'response': False}), 500
        return make_response(jsonify({'response': False, 'erro': 'atividade nao encontrada'}), 400)


'''
Desafio: o que acontece com a sua funcao de atividades quando 
o servidor de pessoas esta caido?
'''
#O servidor sistema_atividades retornará um erro 500, indicando ao usuário que houve um erro interno do servidor
'''
Seria conveniente que o sistema automaticamente considerasse
o professor inválido. Faça isso!
'''
#Feito!


if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0',port=5050)
