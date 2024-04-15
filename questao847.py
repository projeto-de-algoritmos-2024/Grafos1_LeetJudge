from collections import deque

class Solution(object):
  def shortestPathLength(self, graph):
    """
    :type graph: List[List[int]]
    :rtype: int
    """
    n = len(graph)
    dp = [[float('inf')] * n for _ in range(1 << n)]
    for i in range(n):
      dp[1 << i][i] = 0

    q = deque([(i, 1 << i) for i in range(n)])
    while q:
      cur, mask = q.popleft()
      if mask == (1 << n) - 1:
        return dp[mask][cur]  
      for nei in graph[cur]:
        new_mask = mask | (1 << nei)
        if dp[new_mask][nei] > dp[mask][cur] + 1:
          dp[new_mask][nei] = dp[mask][cur] + 1
          q.append((nei, new_mask))
    return -1
