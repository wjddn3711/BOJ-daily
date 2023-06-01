from collections import deque
import sys

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def can_reach(graph, start, visited):
    queue = deque([start])
    visited[start[0]][start[1]] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[x]) and not visited[nx][ny]:
                if graph[nx][ny] == ".":
                    queue.append([nx, ny])
                    visited[nx][ny] = True
                elif graph[nx][ny] == "L":
                    return True
    return False


def day_passed(graph: list):
    x_vectors = []
    melted = []
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == "X":
                x_vectors.append([i, j])

    for x, y in x_vectors:
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[x]):
                if graph[nx][ny] == ".":
                    melted.append([x, y])
                    break
    for x, y in melted:
        graph[x][y] = "."
    return graph


START = []
R, C = map(int, input().split())
pound = []
for i in range(R):
    row = list(input().strip())
    pound.append(row)
    if not START:
        for j in range(len(row)):
            if row[j] == "L":
                START = [i, j]

days = 0
while True:
    visited = [[False] * C for _ in range(R)]
    if can_reach(pound, START, visited):
        break
    days += 1
    pound = day_passed(pound)

print(days)
