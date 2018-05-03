import requests


'''
Nesse arquivo, vamos acessar o servidor "controle_pessoas".

A idéia é que estamos contruindo uma aplicacao "cliente", que está em outro servidor,
mas precisa das informacoes de controle_pessoas.

Devemos, entao, acessar controle_pessoas via rede, nao usar algum tipo de import

(já feito na aula passada)
Crie uma funcao que retorna True 
se um professor leciona uma disciplina
e False caso contrario

Se a disciplina nao existe, retorne :False,'inexistente'
'''

def leciona(id_professor, id_disciplina):
    r = requests.get('http://localhost:5000/leciona/'+str(id_professor)+'/'+str(id_disciplina)+'/')
    if 'leciona' in r.json():
        return r.json()['leciona'] == 'True'
    return False,'inexistente'

'''
Defina uma funcao eh aluno, similar: ela recebe um aluno e uma disciplina,
e retorna True se o aluno faz aquela disciplina, False caso contrario
e (False,'inexistente') se a disciplina nao existe
'''


def eh_aluno(id_aluno, id_disciplina):
    r = requests.get('http://localhost:5000/aluno_de_disciplina/'+str(id_aluno)+'/'+str(id_disciplina)+'/')
    if 'aluno' in r.json():
        return r.json()['aluno'] == 'True'
    return False,'inexistente'


'''
Agora, de runtests.

Se esta tudo ok, (passou teste 005) siga para o arquivo 
sistema_atividades.py
'''


