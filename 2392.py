class Solution(object):
    def buildMatrix(self, k, rowConditions, colConditions):
        """
        :type k: int
        :type rowConditions: List[List[int]]
        :type colConditions: List[List[int]]
        :rtype: List[List[int]]
        """

        # Cria grafo para a ordem das linhas e verifica se é aciclico
        gLinhas = Grafo(k)
        
        for rowCondition in rowConditions:
            gLinhas.adicionaAresta(rowCondition[0],rowCondition[1])
        
        if gLinhas.temCiclo():
            return []

        # Cria grafo para a ordem das colunas e verifica se é aciclico
        gColunas = Grafo(k)
        
        for colCondition in colConditions:
            gColunas.adicionaAresta(colCondition[0],colCondition[1])
        
        if gColunas.temCiclo():
            return []

        # Faz ordenação topologica dos grafos
        ordemLinhas = gLinhas.ordemTopologica()
        ordemColunas = gColunas.ordemTopologica()

        # Cria matriz de zeros
        matriz = [[0] * k for _ in range(k)]

        # Preenche matriz de zeros com numeros obedecendo a ordem topologica
        for i in range(1, k+1):
            m = ordemLinhas.index(i)
            n = ordemColunas.index(i)
            if matriz[m][n] == 0:
                matriz[m][n] = i
            else:
                return []
        return matriz

class Grafo:
    def __init__(self, k):
        self.k = k
        self.grafo = [[] for _ in range(self.k)]

    def adicionaAresta(self, u, v):
        self.grafo[u - 1].append(v)

    def dfs(self, v, visitado, pilhaRecursao):
        visitado[v - 1] = True
        pilhaRecursao[v - 1] = True
        for vizinho in self.grafo[v - 1]:
            if not visitado[vizinho - 1]:
                if self.dfs(vizinho, visitado, pilhaRecursao):
                    return True
            elif pilhaRecursao[vizinho - 1]:
                return True
        pilhaRecursao[v - 1] = False
        return False

    def temCiclo(self):
        visitado = [False] * self.k
        pilhaRecursao = [False] * self.k
        for i in range(self.k):
            if not visitado[i]:
                if self.dfs(i + 1, visitado, pilhaRecursao):
                    return True
        return False

    def ordemTopologica(self):
        visitado = [False] * self.k
        ordem = []
        def dfs_ordem(v):
            visitado[v - 1] = True
            for vizinho in self.grafo[v - 1]:
                if not visitado[vizinho - 1]:
                    dfs_ordem(vizinho)
            ordem.append(v)
        for i in range(self.k):
            if not visitado[i]:
                dfs_ordem(i + 1)
        return ordem[::-1]

    def mostraAdjacencia(self):
        for i in range(self.k):
            print(f'{i+1}:', end='  ')
            for j in self.grafo[i]:
                print(f'{j}  ->', end='  ')
            print('')


sol = Solution()
sol.buildMatrix(3,[[1,2],[2,3],[3,1],[2,3]],[[2,1]])