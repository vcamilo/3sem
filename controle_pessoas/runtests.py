import requests


def existe_id(id_omdb):
	url = "http://www.omdbapi.com/?apikey={}&i={}".format(chave_omdb, id_omdb)
	retorno = req.get(url).json()
	if retorno["Response"] == 'False' :
	  return False
	return True





import unittest

class TestStringMethods(unittest.TestCase):

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

