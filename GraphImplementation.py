from collections import deque

def dfs(graph , visited ,node):
    print(node,end=" ")
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            dfs(graph, visited ,i)

def bfs(graph, visited , V):
    q = deque([1])
    visited[1] = True
    while q:
        node = q.popleft()
        print(node,end=" ")
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                q.append(i)



if __name__ == "__main__":
    V = 4
    graph = [[] for i in range(V+1)]

    graph[1].extend([2,4])
    graph[2].extend([1,3])
    graph[3].extend([2,4])
    graph[4].extend([1,3])

    for i in range(V+1):
        print(f"{i} -> {graph[i]}")
    
    visited = [False] * (V + 1)
    dfs(graph,visited,1)
    print()
    visited_1 = [False] * (V + 1)
    bfs(graph, visited_1 ,V)