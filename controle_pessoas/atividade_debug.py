'''
A função a seguir recebe uma lista e um numero
e promete retornar True quando o numero está na lista

Infelizmente, ela nao faz isso.

Corrija  a função e faça com que ela passe no teste
'''

def busca(lista,numero):
   for e in lista:
       if e == numero:
           return True
   else:
      return False

'''
A seguinte funcao promete retornar se uma lista
é decrescente (cada numero menor ou igual ao anterior)

Infelizmente, ela esta dando uma exception

Corrija a funcao de forma que ela passe no teste
'''

def decrescente(lista):
    for i in range(len(lista)-1):
        if lista[i] < lista[i+1]:
            return False
    return True

'''
A seguinte funcao descreve um texto

Infelizmente, ela esta dando uma exception

Corrija a funcao de forma que ela passe no teste
'''

def descreve(texto):
    resposta = 'Esse livro se chama '
    resposta += texto['titl']
    resposta += ' e foi escrito por '
    resposta += texto['aut']
    resposta += ' no ano de '
    resposta += texto['ano']
    resposta += '. O livro é considerado '
    resposta += texto['adjetivo']
    return resposta






import unittest

class TestStringMethods(unittest.TestCase):
    
    def test_01_busca(self):
        self.assertEqual(busca([1,2,3],1),True) 
        self.assertEqual(busca([1,2,3],2),True) 
        self.assertEqual(busca([1,2,3],3),True) 
        self.assertEqual(busca([1,2,3],4),False) 

    def test_02_decrescente(self):
        self.assertEqual(decrescente([3,2,1]), True)
        self.assertEqual(decrescente([3,2,1,4]), False)

    def test_03_descreve(self):
        texto = {}
        texto['titl'] = 'A volta ao mundo em 80 dias'
        texto['aut'] = 'Julio Verne'
        texto['ano'] = '1800'
        texto['adjetivo'] = 'um classico'
        self.assertEqual( descreve(texto), 'Esse livro se chama A volta ao mundo em 80 dias e foi escrito por Julio Verne no ano de 1800. O livro é considerado um classico')


    

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

