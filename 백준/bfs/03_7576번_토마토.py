# 덱 호출
from collections import deque

# 열과 행을 입력받음(순서주의)
m, n = map(int, input().split())

# 그래프 초기화
graph = []

# 그래프 입력 받음
for i in range(n):
    graph.append(list(map(int, input().split())))

# 초기 익은 토마토의 위치 초기화
tomato_initial_position = []

# 초기 익은 토마토의 위치 저장
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            tomato_initial_position.append([i,j])

# bfs방향 (상,하,좌,우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 큐 초기화
queue = deque()

# 큐에 모든 초기 익은 토마토 위치를 입력함
for i in range(len(tomato_initial_position)):
    queue.append((tomato_initial_position[i][0],tomato_initial_position[i][1]))

while queue:

    (x,y) = queue.popleft()

    for i in range(4):

        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        
        # 토마토가 없는곳은 거르기
        if graph[nx][ny] == -1:
            continue

        if graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx,ny))

# 목표값인 최댓값/ 1은 토마토가 모두 익은 상태이며 가장 빠른 경우.
max_num = 1
# 그래프에 0이 하나라도 있는 경우를 위한 변수 / 헷갈리지 않기 위한 초기값 777
day_0 = 777
for i in range(n):
    for j in range(m):

        # 그래프에 1보다 큰 수가 있으면 그 수가 최댓값이 됨.
        if max_num < graph[i][j]:
            max_num = graph[i][j]

        # 그래프에 0이 단 하나라도 존재할 경우 최소 날짜는 -1
        if graph[i][j] == 0:
            day_0 = -1

# 그래프에 0이 없고, 최댓값이 2보다 큰 경우       
if  day_0 == 777 and max_num >= 2 :
    # 최소날짜는 그래프의 최대값보다 1작아야하므로.
    min_day = max_num - 1

# 그래프에 0이 없고, 최댓값이 1인 경우
elif day_0 == 777 and max_num == 1 :
    # 최소날짜는 0
    min_day = 0

# 그래프에 0 이 있는 경우 즉, day_0 = -1
else:
    min_day = day_0

print(min_day)