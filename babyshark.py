from copy import deepcopy

def find_min(graph,shark_size,shark_pos):
    can_fish = []
    state = [[0 for row in range(n)] for col in range(n)]
    for i in range(n):
        for j in range(n):
            if [i,j] != shark_pos:
                if graph[i][j] > shark_size :
                    state[i][j] = [1,0]
                else :
                    state[i][j] = [0,0]
                    if graph[i][j] !=0 and graph[i][j] != shark_size:
                        can_fish.append([i,j]) # can_fish : possible eaten fish 좌표
            else : state[i][j] = [1,0]
    # dis_map = [[0 for row in range(n)] for col in range(n)]
    sx, sy = shark_pos[0], shark_pos[1]
    state_copy = deepcopy(state)


    min_fish=[]

    for goal in can_fish:
        bfs_queue = [[sx,sy]]
        dis = 0
        cnt = 0
        state = deepcopy(state_copy)
        gx, gy = goal[0], goal[1]

        while bfs_queue:
            x, y = bfs_queue.pop(0)

            if x == gx and y == gy :
                min_fish.append([x,y,state[x][y][1]])
                break
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n : continue
                if(state[nx][ny][0] != 1):

                    bfs_queue.append([nx,ny])

                    state[nx][ny] = [1,state[x][y][1] + 1]

    min_fish = sorted(min_fish, key = lambda x : (x[2],x[0],x[1]))
    # print(min_fish)
    return min_fish


def bfs(graph,shark_pos,shark_size,result,eat_num):
    min_fish = find_min(graph,shark_size,shark_pos)
    # print(min_fish)
    if not min_fish :
        print(result)
        return
    else :
        graph[shark_pos[0]][shark_pos[1]] =  0
        x, y = min_fish[0][0], min_fish[0][1]
        eat_num = eat_num + 1
        if eat_num == shark_size :
            shark_size += 1
            eat_num = 0
        shark_pos = [x, y]
        result = result + min_fish[0][2]
        graph[x][y] = 9
        # print(result)
        bfs(graph,shark_pos,shark_size,result,eat_num)

n = int(input())
# graph = [list(map(int, input().split())) for _ in range(n)]
graph = [[] for _ in range(n)]
for i in range(n):
        graph[i] = list(map(int, input().split()))

shark_pos=[]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9 :
            shark_pos = [i,j]

shark_size = 2
dx = [-1,0,1,0]
dy = [0,-1,0,1]
bfs(graph,shark_pos,2,0,0)
