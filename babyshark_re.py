
def bfs(graph, shark_pos, shark_size, time):
    ans = 0
    eat_num = 0
    queue, visited = [shark_pos], [shark_pos]
    while queue:
        # print(queue)
        queue = sorted(queue,key = lambda x : (x[0],x[1]))
        size = len(queue)
        flag = False
        for _ in range(size):
            sx, sy = queue.pop(0)
            if graph[sx][sy] != 0 and graph[sx][sy] < shark_size :
                flag = True
                eat_num += 1
                graph[sx][sy] = 0
                # print(sx,sy)
                if eat_num == shark_size :
                    shark_size += 1
                    eat_num = 0
                ans = time
                queue, visited = [], [[sx,sy]]

            for i in range(4):
                nx = sx + dx[i]
                ny = sy + dy[i]
                if 0 <= nx < n and 0 <= ny < n and [nx,ny] not in visited:
                    if graph[nx][ny] <= shark_size :
                        queue.append([nx,ny])
                        visited.append([nx,ny])

            if flag:
                flag = False
                break
        time += 1
    return ans






n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9 :
            shark_pos = [i,j]
            graph[i][j] = 0


dx = [-1,0,0,1]
dy = [0,-1,1,0]
print(bfs(graph,shark_pos,2,0))
