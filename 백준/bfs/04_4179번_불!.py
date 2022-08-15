from collections import deque

r, c = map(int, input().split())

graph = [[] * c for _ in range(r)]
jgraph = [[] * c for _ in range(r)]

graph_input = []
for i in range(r):
    graph_input.append(input())

fire_position = []
j_position = []

for i in range(r):
    for j in range(c):
        graph[i].append(graph_input[i][j])
        jgraph[i].append(graph_input[i][j])

        if graph_input[i][j] == 'F':
            fire_position.append([i,j])
            graph[i][j] = 0

        if graph_input[i][j] == 'J':
            j_position.append([i,j])
            jgraph[i][j] = 0      

queue = deque()

if len(fire_position) >= 1:
    for i in range(len(fire_position)):
        queue.append((fire_position[i][0],fire_position[i][1]))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    
    (x, y) = queue.popleft()

    for i in range(4):

        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or ny < 0 or nx >= r or ny >= c:
            continue

        if graph[nx][ny] == '.':
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx, ny))

jqueue = deque()

jqueue.append((j_position[0][0],j_position[0][1]))

jcount = 0

while jqueue:
    
    (x, y) = jqueue.popleft()

    for i in range(4):

        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or ny < 0 or nx >= r or ny >= c:
            jcount = jgraph[x][y] + 1
            continue

        if jgraph[nx][ny] == '.' or type(graph[nx][ny]) is int:
            jgraph[nx][ny] = jgraph[x][y] + 1
            if (jgraph[x][y] + 1) < graph[nx][ny]:
                jqueue.append((nx, ny))
    
    if jcount != 0:
        break

judge = 0

for i in range(r):
    for j in range(c):
        if (i == 0 or i == r-1 or j == 0 or j == c-1) and type(jgraph[i][j]) == int:
            judge = 1

if judge == 0: 
    print('IMPOSSIBLE')
else:
    print(jcount)