from collections import deque

def shortestPathLength(graph):
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

# Examplo 1
graph = [[1,2,3],[0],[0],[0]]
print(shortestPathLength(graph))  # Output: 4

# Examplo 2
graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
print(shortestPathLength(graph))  # Output: 4