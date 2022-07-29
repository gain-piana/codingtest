# deque 사용을 위한 호출
from collections import deque

# 행과 열을 입력 받기
n, m = map(int, input().split())

# 그래프 초기화
graph = [[] * m for _ in range(n)]

# 입력예시를 받기위한 임시리스트
input_ex = []

# 임시리스트에 입력예시 저장
for i in range(n):
    input_ex.append(input())

# 그래프에 임시리스트 값들을 저장
for i in range(n):
    for j in range(m):
        graph[i].append(int(input_ex[i][j]))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = deque()
queue.append((0,0))

while queue:

    (x,y) = queue.popleft()

    for i in range(4):

        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m or (nx == 0 and ny == 0):
            continue

        if graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx,ny))

# 문제에서 도착지가 n,m으로 고정되어 있으므로.
print(graph[n-1][m-1])