class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """

        gAlice = Grafo(n)
        gBob = Grafo(n)
        gAmbos = Grafo(n)

        for edge in edges:
            if edge[0]==1:
                gAlice.adicionaAresta(edge[1],edge[2])
            elif edge[0]==2:
                gBob.adicionaAresta(edge[1],edge[2])
            else:
                gAmbos.adicionaAresta(edge[1],edge[2])



        print("==================== Alice ==================== ", gAlice.calculaNumArestas())
        gAlice.mostraAdjacencia()
        print("===================== Bob ===================== ", gBob.calculaNumArestas())
        gBob.mostraAdjacencia()
        print("==================== Ambos ==================== ", gAmbos.calculaNumArestas())
        gAmbos.mostraAdjacencia()


class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]

    def adicionaAresta(self, u, v):
        self.grafo[u-1].append(v)
        self.grafo[v-1].append(u)

    def removeAresta(self, u, v):
        if v in self.grafo[u-1]:
            self.grafo[u-1].remove(v)
        if u in self.grafo[v-1]:
            self.grafo[v-1].remove(u)

    def calculaNumArestas(self):
        somaGraus = sum(len(adj) for adj in self.grafo)
        return somaGraus // 2

    # def grau(self, u):
    #     return len(self.grafo[u-1])

    # def listaNosGrauZero(self):
    #     nosGrauZero = []
    #     for i in range(1, self.vertices + 1):
    #         if self.grau(i) == 0:
    #             nosGrauZero.append(i)
    #     return nosGrauZero

    def mostraAdjacencia(self):
        for i in range(self.vertices):
            print(f'{i+1}:', end='  ')
            for j in self.grafo[i]:
                print(f'{j}  ->', end='  ')
            print('')

sol = Solution()
sol.maxNumEdgesToRemove(4, [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]])
