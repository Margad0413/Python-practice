def dfs(graph, vertex, visited, start):
    visited[start] = True
    print(vertex[start], end=' ') #방문 노드 출력

    # 인접한 노드를 알파벳 순서대로 탐색
    for i in range(len(graph[start])):
        if graph[start][i] == 1 and not visited[i]: #방문했으며, 리스트에 없는 값 찾기
            dfs(graph, vertex, visited, i) #자기자신 다시 호출출

vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
adjMat = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0]
]

# 방문 여부를 저장하는 리스트
visited = [False] * len(vertex)
dfs(adjMat, vertex, visited, 0) #A부터 시작하기 때문에 0
