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
    

    def test_003_estuda(self):
        r = requests.get('http://localhost:5000/aluno_de_disciplina/10/1/')
        self.assertEqual(r.json(),{'aluno':'True','response':'True'})
        r = requests.get('http://localhost:5000/aluno_de_disciplina/10/2/')
        self.assertEqual(r.json(),{'aluno':'False','response':'True'})
        r = requests.get('http://localhost:5000/aluno_de_disciplina/1/1/')
        self.assertEqual(r.json(),{'aluno':'False','response':'True'})
        r = requests.get('http://localhost:5000/aluno_de_disciplina/3/2/')
        self.assertEqual(r.json(),{'aluno':'False','response':'True'})
    
    def test_004_disciplina_not_found_for_aluno(self):
        r = requests.get('http://localhost:5000/aluno_de_disciplina/1/100/')
        self.assertEqual(r.json()['response'],'False')
        self.assertEqual(r.json(),{'response':'False', 'error':'disciplina nao encontrada'})
        self.assertEqual(r.status_code,404)
    
    def test_005_metodo_eh_aluno(self):
        self.assertEqual(acesso.eh_aluno(10,1),True)
        self.assertEqual(acesso.eh_aluno(10,2),False)
        self.assertEqual(acesso.eh_aluno(1,200),(False,'inexistente'))
    
    def test_006_textos_forum(self):
        r = requests.get('http://localhost:5050/forum/2/')
        self.assertEqual(r.json()['response'],False)
        r = requests.get('http://localhost:5050/forum/2/?professor=3')
        self.assertEqual(r.json()['response'],True)
        self.assertEqual(r.json()['textos'][0][0]['texto'],'nao entendi nada sobre juros')
        r = requests.get('http://localhost:5050/forum/1/?aluno=10')
        self.assertEqual(r.json()['response'],True)
        self.assertEqual(r.json()['textos'][0][0]['texto'],'voces entenderam o exercicio?')
        r = requests.get('http://localhost:5050/forum/2/?professor=1')
        self.assertEqual(r.json()['response'],False)


    def test_007_participantes(self):
        r = requests.get('http://localhost:5050/forum/2/?professor=3')
        self.assertEqual(r.json()['response'],True)
        self.assertTrue('maria' in r.json()['participantes'])
        self.assertTrue('miguel' in r.json()['participantes'])
        self.assertTrue(len(r.json()['participantes']) == 2)

    

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

