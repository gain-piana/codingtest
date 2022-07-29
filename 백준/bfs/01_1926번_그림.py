from collections import deque

n, m = map(int,input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

visited = [[0] * m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = deque()

count = 2

max_num = [0]
for k in range(n):
    for l in range(m):
        
        num = 0
        if graph[k][l] == 1 and visited[k][l] == 0:
            visited[k][l] = 1

            queue.append((k,l))

            while queue:
            
                x,y = queue.popleft()
                num += 1
                for i in range(4):
            
                    nx = x + dx[i]
                    ny = y + dy[i]

                    
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        continue
                    if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        queue.append((nx,ny))
            max_num.append(num)
print(len(max_num)-1)
print(max(max_num))