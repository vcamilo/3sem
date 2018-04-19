import requests as req


'''
Crie uma funcao que retorna True 
se um professor leciona uma disciplina
e False caso contrario

Se a disciplina nao existe, retorne :False,'inexistente'
'''

def leciona(id_professor, id_disciplina):
    url = "http://localhost:5000/leciona/{}/{}".format(id_professor, id_disciplina)
    retorno = req.get(url).json()
    if retorno['response']:
        return True
    return False
    

'''
Agora, de runtests.

Se esta tudo ok, (passou teste 002) siga para o arquivo 
sistema_atividades.py

A atividade de 07 de marco pode ser util para lembrar como usar a biblioteca requests
'''

