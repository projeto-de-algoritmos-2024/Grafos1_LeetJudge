from questao797 import Solution
import unittest

class TestAllPathsSourceTarget(unittest.TestCase):
    def test_exemple_1(self):
        s = Solution()
        saida = s.allPathsSourceTarget([[1,2],[3],[3],[]])
        esperado = [[0,1,3],[0,2,3]]
        self.assertEqual(saida, esperado)
    
    def test_exemple_2(self):
        s = Solution()
        saida = s.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]])
        esperado = [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
        self.assertEqual(saida, esperado)


if __name__ == '__main__':
    unittest.main()
