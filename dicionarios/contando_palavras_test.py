import unittest
from contando_palavras import contando_palavras

__unittest = True

class FunctionTest(unittest.TestCase):

    def test_exemplo(self):

            palavras = ["abacaxi", "jupiter", "marte", "marte", "abacate", "jupiter", "estrela", "pessoa"]
            palavra_escolhida = "jupiter"
            expect = 2
            actual = contando_palavras(palavras, palavra_escolhida)
            failure_msg = 'Should return {0} but returned {1}'
            self.assertEqual(actual, expect, failure_msg.format(expect, actual))
    
    def test_palavra_inexistente(self):
            palavras = ["abacaxi", "jupiter", "marte", "marte", "abacate", "jupiter", "estrela", "pessoa"]
            palavra_escolhida = "laranja"
            expect = 0
            actual = contando_palavras(palavras, palavra_escolhida)
            failure_msg = 'Should return {0} but returned {1}'
            self.assertEqual(actual, expect, failure_msg.format(expect, actual))
    
    def test_palavras_iguais(self):
            palavras = ["abacaxi", "abacaxi", "abacaxi", "abacaxi", "abacaxi", "abacaxi", "abacaxi", "abacaxi"]
            palavra_escolhida = "abacaxi"
            expect = 8
            actual = contando_palavras(palavras, palavra_escolhida)
            failure_msg = 'Should return {0} but returned {1}'
            self.assertEqual(actual, expect, failure_msg.format(expect, actual))

if __name__ == "__main__":
    unittest.main()
