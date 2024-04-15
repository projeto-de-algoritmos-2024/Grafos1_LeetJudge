def allPathsSourceTarget(graph):
    def dfs(node, path):
        if node == len(graph) - 1:
            res.append(path)
            return
        for nei in graph[node]:
            dfs(nei, path + [nei])

    res = []
    dfs(0, [0])
    return res

# Examplos:
graph1 = [[1,2],[3],[3],[]]
graph2 = [[4,3,1],[3,2,4],[3],[4],[]]

print(allPathsSourceTarget(graph1))  # Output: [[0,1,3],[0,2,3]]
print(allPathsSourceTarget(graph2))  # Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]

