from copy import deepcopy
def dfs(graph,fish,shark_x,shark_y,eat_num):
    #copy init_state using deepcopy
    global res_num
    graph,fish = deepcopy(graph),deepcopy(fish)
    fish_num = graph[shark_x][shark_y][0]
    shark_dir = graph[shark_x][shark_y][1]
    fish[fish_num] = [-1,-1]
    graph[shark_x][shark_y][0] = -1
    eat_num = eat_num + fish_num

    #fish move according to fish order 1,2,3,4 ......
    for i in range(1,17):
        if fish[i] != [-1,-1]:

            fish_x, fish_y = fish[i][0], fish[i][1]
            fish_dir = graph[fish_x][fish_y][1] - 1
            # print(i,fish_dir,shark_x,shark_y)
            for j in range(8):

                nx = fish_x + dx[(fish_dir+j) % 8]
                ny = fish_y + dy[(fish_dir+j) % 8]
                if(nx < 0 or nx >= 4 or ny < 0 or ny >= 4 or (nx == shark_x and ny == shark_y)) : continue

                if(graph[nx][ny] == [-1,-1]):
                    fish[i] = [nx,ny]
                    graph[fish_x][fish_y][1] = (fish_dir + j) % 8 + 1
                    graph[nx][ny], graph[fish_x][fish_y] = graph[fish_x][fish_y], graph[nx][ny]

                    break
                else:

                    fish[graph[nx][ny][0]], fish[i] = fish[i], fish[graph[nx][ny][0]]
                    graph[fish_x][fish_y][1] = (fish_dir + j) % 8 + 1
                    graph[nx][ny], graph[fish_x][fish_y] = graph[fish_x][fish_y], graph[nx][ny]
                    # print(copy_graph)
                    break

    for i in range(1,4):

        shark_nx = shark_x + dx[shark_dir-1] * i
        shark_ny = shark_y + dy[shark_dir-1] * i
        if(shark_nx < 0 or shark_nx >= 4 or shark_ny < 0 or shark_ny >= 4) :
            res_num = max(res_num,eat_num)
            break
        if graph[shark_nx][shark_ny] != [-1,-1]:
            graph[shark_x][shark_y]=[-1,-1]
            dfs(graph,fish,shark_nx,shark_ny,eat_num)

# input

graph = [[[] for row in range(4)] for col in range(4)]
fish = [[] for _ in range (17)]
for i in range(4):
    temp = list(map(int,input().split()))

    for j in range(4):
        graph[i][j] = [temp[j*2],temp[j*2+1]]
        fish[temp[j*2]] = [i,j]

dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,-1,-1,-1,0,1,1,1]
res_num = 0
# print(graph)
# print(fish)
dfs(graph,fish,0,0,0)
print(res_num)
