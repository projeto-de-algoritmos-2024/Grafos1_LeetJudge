from questao332 import Solution
import unittest

class TestFindItinerary(unittest.TestCase):
    def test_exemple_1(self):
        s = Solution()
        saida = s.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]])
        esperado = ["JFK","MUC","LHR","SFO","SJC"]
        self.assertEqual(saida, esperado)
    
    def test_exemple_2(self):
        s = Solution()
        saida = s.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])
        esperado = ["JFK","ATL","JFK","SFO","ATL","SFO"]
        self.assertEqual(saida, esperado)


if __name__ == '__main__':
    unittest.main()
