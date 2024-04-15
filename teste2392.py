from questao2392 import Solution
import unittest

class TestBuildMatrix(unittest.TestCase):
    def test_exemple_1(self):
        s = Solution()
        saida = s.buildMatrix(3, [[1,2],[3,2]], [[2,1],[3,2]])
        esperado = [[3,0,0],[0,0,1],[0,2,0]]
        self.assertEqual(saida, esperado)
    
    def test_exemple_2(self):
        s = Solution()
        saida = s.buildMatrix(3, [[1,2],[2,3],[3,1],[2,3]], [[2,1]])
        esperado = []
        self.assertEqual(saida, esperado)


if __name__ == '__main__':
    unittest.main()



