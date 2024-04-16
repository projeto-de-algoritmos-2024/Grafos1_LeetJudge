import collections

class Solution(object):
    def __init__(self):
        self.grafo = Grafo()
        self.rota = []

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        for a, b in sorted(tickets, reverse=True):
            self.grafo.adicionaAresta(a, b)
        
        self.visita('JFK')
        
        return self.rota[::-1]

    def visita(self, aeroporto):
        while self.grafo.objetivos[aeroporto]:
            self.visita(self.grafo.objetivos[aeroporto].pop())
        self.rota.append(aeroporto)


class Grafo:
    def __init__(self):
        self.objetivos = collections.defaultdict(list)

    def adicionaAresta(self, u, v):
        self.objetivos[u].append(v)
