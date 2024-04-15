def findSmallestSetOfVertices(n, edges):
    # Inicialize um conjunto para armazenar vértices sem arestas da entrada
    no_incoming_edges = set(range(n))
    
    # Iterar pelas arestas e remover vértices com arestas de entrada
    for _, to_vertex in edges:
        if to_vertex in no_incoming_edges:
            no_incoming_edges.remove(to_vertex)
    
    # Converta o conjunto em uma lista e retorna
    return list(no_incoming_edges)

# Examplo 1
n1 = 6
edges1 = [[0,1],[0,2],[2,5],[3,4],[4,2]]
print(findSmallestSetOfVertices(n1, edges1)) # Output: [0, 3]

# Examplo 2
n2 = 5
edges2 = [[0,1],[2,1],[3,1],[1,4],[2,4]]
print(findSmallestSetOfVertices(n2, edges2)) # Output: [0, 2, 3]
