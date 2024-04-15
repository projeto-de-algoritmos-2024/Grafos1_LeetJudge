class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        def dfs(node, path):
            if node == len(graph) - 1:
                res.append(path)
                return
            for nei in graph[node]:
                dfs(nei, path + [nei])

        res = []
        dfs(0, [0])
        return res

