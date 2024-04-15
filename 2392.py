class Solution(object):
    def buildMatrix(self, k, rowConditions, colConditions):
        """
        :type k: int
        :type rowConditions: List[List[int]]
        :type colConditions: List[List[int]]
        :rtype: List[List[int]]
        """

        gLinhas = Grafo(k)
        gColunas = Grafo(k)

        for rowCondition in rowConditions:
            gLinhas.adicionaAresta(rowCondition[0],rowCondition[1])

        for colCondition in colConditions:
            gColunas.adicionaAresta(colCondition[0],colCondition[1])

        ordemLinhas = gLinhas.ordemTopologica()
        ordemColunas = gColunas.ordemTopologica()

        matriz = [[0] * k for _ in range(k)]

        for i in range(1, k+1):
            m = ordemLinhas.index(i)
            n = ordemColunas.index(i)
            if matriz[m][n] == 0:
                matriz[m][n] = i
            else:
                return []

        print(matriz)
        print("==================== Linha ==================== ", gLinhas.ordemTopologica())
        gLinhas.mostraAdjacencia()
        print("===================== Coluna ===================== ", gColunas.ordemTopologica())
        gColunas.mostraAdjacencia()

        return matriz




class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]

    def adicionaAresta(self, u, v):
        self.grafo[u-1].append(v)
        # self.grafo[v-1].append(u)

    def dfs(self, v, visitado, stack):
        visitado[v - 1] = True
        for vizinho in self.grafo[v - 1]:
            if not visitado[vizinho - 1]:
                self.dfs(vizinho, visitado, stack)
        stack.append(v)

    def ordemTopologica(self):
        visitado = [False] * self.vertices
        stack = []
        for i in range(self.vertices):
            if not visitado[i]:
                self.dfs(i + 1, visitado, stack)
        return stack[::-1]

    def mostraAdjacencia(self):
        for i in range(self.vertices):
            print(f'{i+1}:', end='  ')
            for j in self.grafo[i]:
                print(f'{j}  ->', end='  ')
            print('')

sol = Solution()
sol.buildMatrix(3,[[1,2],[2,3],[3,1],[2,3]],[[2,1]])