from questao847 import Solution
import unittest

class TestShortestPathLength(unittest.TestCase):
    def test_exemple_1(self):
        s = Solution()
        saida = s.shortestPathLength([[1,2,3],[0],[0],[0]])
        esperado = 4
        self.assertEqual(saida, esperado)
    
    def test_exemple_2(self):
        s = Solution()
        saida = s.shortestPathLength([[1],[0,2,4],[1,3,4],[2],[1,2]])
        esperado = 4
        self.assertEqual(saida, esperado)


if __name__ == '__main__':
    unittest.main()
