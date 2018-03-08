def soma_pa_rec(n):
  if n <= 0:
    return n
  return n+soma_pa_rec(n-1)
  
print(soma_pa_rec(100))

import unittest
import sys

class TestStringMethods(unittest.TestCase):

    def test_000_soma_pa_funciona(self):
       self.assertEqual(soma_pa_rec(3) , 6 )
       self.assertEqual(soma_pa_rec(5) , 15 )
       self.assertEqual(soma_pa_rec(100) , 5050 )
       self.assertEqual(soma_pa_rec(1) , 1)
    
    def test_001_soma_pa_eh_recursiva(self):
        sys.setrecursionlimit(50)
        try:
            soma_pa_rec(100)
            self.fail('a sua função é recursiva?')
        except RecursionError:
            print('')
            print('correto, sua funcao é recursiva')
        finally:
            sys.setrecursionlimit(1000)
    
    def test_01_soma_funciona(self):
        self.assertEqual(soma_recursiva([1,2,3]),6)
        self.assertEqual(soma_recursiva([1,2,3,4]),10)
        self.assertEqual(soma_recursiva([-1,-2,-3,-4]),-10)
    
    def test_02_soma_pequena(self):
        self.assertEqual(soma_recursiva([1]),1)
        self.assertEqual(soma_recursiva([]),0)
        self.assertEqual(soma_recursiva([-3]),-3)

    def test_03_soma_recursivo(self):
        sys.setrecursionlimit(50)
        try:
            soma_recursiva([1]*100)
            self.fail('a sua função é recursiva?')
        except RecursionError:
            print('')
            print('correto, sua funcao é recursiva')
        finally:
            sys.setrecursionlimit(1000)
    
    def test_04_conta(self):
         self.assertEqual(conta_recursiva([0,1,2,1,4],1), 2)
         self.assertEqual(conta_recursiva([0,1,2,1,4],4), 1)
         self.assertEqual(conta_recursiva([1,1],1), 2)
         self.assertEqual(conta_recursiva([1,1],2), 0)
         self.assertEqual(conta_recursiva([0,1,2,1,4],5), 0)
   
    def test_05_conta_pequena(self):
         self.assertEqual(conta_recursiva([],5), 0)
         self.assertEqual(conta_recursiva([5],5), 1)
         self.assertEqual(conta_recursiva([1],5), 0)
    
    def test_06_conta_recursiva(self):
        sys.setrecursionlimit(50)
        try:
            conta_recursiva([1]*100,1)
            self.fail('a sua função é recursiva?')
        except RecursionError:
            print('')
            print('correto, sua funcao é recursiva')
        finally:
            sys.setrecursionlimit(1000)
    
    def test_07_filtro(self):
         self.assertEqual(filtro_recursivo([0,1,2,1,4],1), [0,2,4])
         self.assertEqual(filtro_recursivo([0,1,2,1,4],4), [0,1,2,1])
         self.assertEqual(filtro_recursivo([1,1],1), [])
         self.assertEqual(filtro_recursivo([1,1],2), [1,1])
         self.assertEqual(filtro_recursivo([0,1,2,1,4],5), [0,1,2,1,4])
   
    def test_08_filtro_pequeno(self):
         self.assertEqual(filtro_recursivo([],5), [])
         self.assertEqual(filtro_recursivo([1],5), [1])
    
    def test_09_filtro_recursivo(self):
        sys.setrecursionlimit(50)
        try:
            filtro_recursivo([1]*100,1)
            self.fail('a sua função é recursiva?')
        except RecursionError:
            print('')
            print('correto, sua funcao é recursiva')
        finally:
            sys.setrecursionlimit(1000)

    def test_10_palindromo(self):    
        self.assertEqual(palindromo_recursivo('abbabba'), True)
        self.assertEqual(palindromo_recursivo('aaa') , True)
        self.assertEqual(palindromo_recursivo('aaaa') , True)
        self.assertEqual(palindromo_recursivo('aac') , False)

    def test_11_palindromo_peq(self):    
        self.assertEqual(palindromo_recursivo('a') , True)
        self.assertEqual(palindromo_recursivo('') , True)
    
    def test_12_palindromo_recursivo(self):
        sys.setrecursionlimit(50)
        try:
            palindromo_recursivo('a'*100)
            self.fail('a sua função é recursiva?')
        except RecursionError:
            print('')
            print('correto, sua funcao é recursiva')
        finally:
            sys.setrecursionlimit(1000)
    
    def test_13_troca(self):
         self.assertEqual(troca_recursiva([0,1,2,1,4],1,7), [0,7,2,7,4])
         self.assertEqual(troca_recursiva([0,1,2,1,4],4,9), [0,1,2,1,9])
         self.assertEqual(troca_recursiva([1,1],1,2), [2,2])
         self.assertEqual(troca_recursiva([1,1],2,7), [1,1])
         self.assertEqual(troca_recursiva([0,1,2,1,4],5,3), [0,1,2,1,4])
         self.assertEqual(troca_recursiva([0,1,2,1,4],0,0), [0,1,2,1,4])
         self.assertEqual(troca_recursiva([0,1,2,1,4],9,9), [0,1,2,1,4])
   
    def test_14_troca_pequeno(self):
         self.assertEqual(troca_recursiva([],5,2), [])
         self.assertEqual(troca_recursiva([1],5,4), [1])
         self.assertEqual(troca_recursiva([5],5,4), [4])
    
    def test_15_troca_recursivo(self):
        sys.setrecursionlimit(50)
        try:
            troca_recursiva([1]*100,1,2)
            self.fail('a sua função é recursiva?')
        except RecursionError:
            print('')
            print('correto, sua funcao é recursiva')
        finally:
            sys.setrecursionlimit(1000)




    def test_91_anagramas(self):
        a = anagramas('abc')
        self.assertEqual(set(a),set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))
        a = anagramas('abcd')
        self.assertEqual(set(a),set(['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba']))
        a = anagramas('abca')
        self.assertEqual(set(a),set(['abca', 'abac', 'acba', 'acab', 'aabc', 'aacb', 'baca', 'baac', 'bcaa', 'bcaa', 'baac', 'baca', 'caba', 'caab', 'cbaa', 'cbaa', 'caab', 'caba', 'aabc', 'aacb', 'abac', 'abca', 'acab', 'acba']))




    


    
    

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

import unittest

    
    

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

'''
submeter em:
https://goo.gl/vECTso
'''
