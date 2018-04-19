import requests
import acesso







import unittest

class TestStringMethods(unittest.TestCase):

    def test_000_leciona(self):
        r = requests.get('http://localhost:5000/leciona/1/1/')
        self.assertEqual(r.json(),{'leciona':'True','response':'True'})
        r = requests.get('http://localhost:5000/leciona/100/1/')
        self.assertEqual(r.json(),{'leciona':'False','response':'True'})
    
    def test_001_leciona_not_found(self):
        r = requests.get('http://localhost:5000/leciona/1/100/')
        self.assertEqual(r.json()['response'],'False')
        self.assertEqual(r.json(),{'response':'False', 'error':'disciplina nao encontrada'})
        self.assertEqual(r.status_code,404)
    
    def test_002_metodo_leciona(self):
        self.assertEqual(acesso.leciona(1,1),True)
        self.assertEqual(acesso.leciona(100,1),False)
        self.assertEqual(acesso.leciona(1,200),(False,'inexistente'))
    
    def test_003_atividade(self):
        r = requests.get('http://localhost:5050/atividade/1/')
        self.assertEqual(r.json()['atividade']['enunciado'], "crie um app de todo em flask")
        r = requests.get('http://localhost:5050/atividade/2/')
        self.assertEqual(r.json()['atividade']['enunciado'], "crie um servidor que envia email em Flask")
    
    def test_004_atividade_not_found(self):
        r = requests.get('http://localhost:5050/atividade/123/')
        self.assertEqual(r.json()['response'], "False")
        self.assertEqual(r.status_code,404)

    def test_005_atividade_boas_praticas(self):
        r = requests.get('http://localhost:5050/atividade/1/')
        self.assertEqual(r.json()['response'],'True')
        self.assertEqual(r.json()['atividade']['url'],'/atividade/1/')
        r = requests.get('http://localhost:5050/atividades/ver_tudo/')
        self.assertEqual('enunciado' in r.json()[0],True)
        self.assertEqual('url' in r.json()[0],False)
    
    
    def test_006_atividade_professor(self):
        r = requests.get('http://localhost:5050/atividade/1/')
        self.assertFalse('respostas' in r.json()['atividade'])
        r = requests.get('http://localhost:5050/atividade/1/', params={'id_professor':100})
        self.assertFalse('respostas' in r.json()['atividade'])
        r = requests.get('http://localhost:5050/atividade/1/', params={'id_professor':1})
        self.assertTrue('respostas' in r.json()['atividade'])

class TestiUnused(unittest.TestCase):


    def test_00_adiciona(self):
        requests.post('http://localhost:5000/professores/',json={'nome':'robotinik'})
        r = requests.get('http://localhost:5000/pessoas/ver_tudo/')
        self.assertEqual(r.json()[0][-1]['nome'],'robotinik')
        self.assertFalse('url' in r.json()[0][-1])
        

    def test_01_adiciona_resposta(self):
        r = requests.post('http://localhost:5000/professores/',json={'nome':'roboto'})
        self.assertEqual(r.json()['professor']['nome'],'roboto')
        self.assertEqual(r.json()['response'],'True')
        self.assertEqual(r.status_code,201)



    def test_02_adiciona_boas_praticas(self):
        r = requests.post('http://localhost:5000/professores/',json={'nome':'roboto'})
        self.assertTrue('url' in r.json()['professor'])
        self.assertTrue('/professor/' in r.json()['professor']['url'])

    def test_03_adiciona_bons_erros(self):
        r = requests.post('http://localhost:5000/professores/',json={'nome':''})
        self.assertEqual(r.status_code,400)
        self.assertEqual(r.json()['response'],'False')
        r = requests.post('http://localhost:5000/professores/',json={})
        self.assertEqual(r.status_code,400)
        self.assertEqual(r.json()['response'],'False')
    
    def test_04_aluno_by_id(self):
        r = requests.get('http://localhost:5000/aluno/2')
        self.assertEqual(r.json()['aluno']['nome'],'miguel')
    
    def test_05_aluno_inexistente(self):
        r = requests.get('http://localhost:5000/aluno/500')
        self.assertEqual(r.json()['response'],'False')
        self.assertEqual(r.status_code,404)

    def test_06_aluno_by_id_boas_praticas(self):
        r = requests.get('http://localhost:5000/aluno/2')
        self.assertEqual(r.json()['response'],'True')
        self.assertEqual(r.status_code,200)
        self.assertTrue('url' in r.json()['aluno'])
        r = requests.get('http://localhost:5000/pessoas/ver_tudo/')
        self.assertTrue('url' not in r.json()[1][1])
    
    def test_07_disciplina_by_id(self):
        r = requests.get('http://localhost:5000/disciplina/2')
        self.assertEqual(r.json()['disciplina']['nome'],'matematica financeira')
    
    def test_08_disciplina_by_name(self):
        r = requests.get('http://localhost:5000/disciplina/busca/',params={'busca':'matematica'})
        self.assertEqual(len(r.json()['disciplinas']), 2)
        self.assertTrue('url' in r.json()['disciplinas'][0])
        self.assertEqual(r.json()['response'],'True')
    
    def test_09_disciplina_by_name_sem_query(self):
        r = requests.get('http://localhost:5000/disciplina/busca/',params={'buscar':'matematica'})
        self.assertEqual(r.json()['response'],'False')
        self.assertEqual(r.status_code,400)



    

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

