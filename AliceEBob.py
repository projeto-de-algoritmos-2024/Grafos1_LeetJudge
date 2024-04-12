class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        
        g_alice = Grafo(n)
        g_bob = Grafo(n)

        for edge in edges:
            if edge[0]==1 or edge[0]==3:
                g_alice.adiciona_aresta(edge[1],edge[2])
            if edge[0]==2 or edge[0]==3:
                g_bob.adiciona_aresta(edge[1],edge[2])
        



class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]

    def adiciona_aresta(self, u, v):
        self.grafo[u-1].append(v)
        self.grafo[v-1].append(u)

    def mostra_lista(self):
        for i in range(self.vertices):
            print(f'{i+1}:', end='  ')
            for j in self.grafo[i]:
                print(f'{j}  ->', end='  ')
            print('')        