from collections import deque


def bfs(start_node, graph, n):
    visited = [False] * (n + 1)
    
    temp = start_node
    deq = deque()
    
    
    deq.append(temp)
    
    # visited[start_node] = True
    
    while deq:
        
        temp = deq.popleft()
        
        for edge in graph:
            if edge[0] == temp:
                if visited[edge[1]] == False:
                    deq.append(edge[1])
                    visited[edge[1]] = True
    
    return visited[start_node]    
                                           


def perfectWalk(n, m, graph):
    perfect_walk = [0] * (n + 1)
    for i in range(1, n + 1):
        perfect_walk[i] = bfs(i, graph, n)
        var = bfs(i, graph, n)
        if var:
            perfect_walk[i] = 1
            
    perfect_walk.pop()
    return perfect_walk

        

