
def bfs():
    time = 0
    shark_num = len(shark)

    # smell = [[] for _ in range(k)]

    while(1):
        # print("dsfasd")
        # crash_shark = []
        # queue = []
        # visited = []
        keys = list(shark.keys())
        keys.sort()
        time = time + 1
        for index in keys:
            flag_blank = 0
            # shark_no = index[0]-1
            x = shark[index][0]
            y = shark[index][1]
            dir = shark[index][2]
            move_rank = dir_rank[(index-1) * 4 + dir - 1]
            for d in move_rank:
                nx, ny = x + dx[d-1], y + dy[d-1]
                if(0 <= nx < n and 0 <= ny < n):
                    if(board[nx][ny] == [0,0]):
                        shark[index] = [nx,ny,d]
                        # board[nx][ny] = [shark_no + 1, k]
                        # board[x][y]
                        # if [nx,ny] in visited:
                        #     crash_shark.append(shark_no)
                        # else :
                        #     visited.append([nx,ny])
                        #     queue.append([shark_no + 1,nx,ny])
                        #     shark_dir[shark_no] = d
                        flag_blank = 1
                        break
            if(flag_blank == 0):
                flag_smell = 0
                for d in move_rank:
                    nx, ny = x + dx[d-1], y + dy[d-1]
                    if(0 <= nx < n and 0 <= ny < n):
                        if(board[nx][ny][0] == index):
                            flag_smell = 1
                            shark[index] = [nx,ny,d]
                            # board[nx][ny] = [shark_no + 1, k]
                            # if [nx,ny] in visited:
                            #     crash_shark.append(shark_no)
                            # else :
                            #     visited.append([nx,ny])
                            #     queue.append([shark_no + 1,nx,ny])
                            #     shark_dir[shark_no] = d
                            break
                if flag_smell == 0 :
                    del shark[index]
        for i in range(n):
            for j in range(n):
                if board[i][j][0] != 0 :
                    board[i][j][1] -= 1
                    if(board[i][j][1] == 0):
                        board[i][j] =[0,0]
        for index in keys :
            x, y = shark[index][0], shark[index][1]
            if board[x][y] == [0,0]:
                board[x][y] = [index,k]
            elif board[x][y][0] == index:
                board[x][y] = [index,k]
            else :
                del shark[index]

        # for a in queue:
        #     board[a[1]][a[2]] = [a[0],k]
        #     for i in range(len(shark_pos)):
        #         if shark_pos[i][0] == a[0]:
        #             shark_pos[i] = [a[0],a[1],a[2]]
        # for c in crash_shark:
        #     for i in range(len(shark_pos)):
        #         if shark_pos[i][0] == c+1:
        #             del shark_pos[i]
            # shark_pos.pop(c)
        shark_num = len(shark)
        # print(shark_num)
        # if(time == 4): break
        if(time > 1000):
            return -1
        if shark_num == 1 : break
    return time

    # return time
n,m,k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
shark_dir = list(map(int,input().split()))
dir_rank = [list(map(int,input().split())) for _ in range(m*4)]
shark = {}
# print(dir_rank)
shark_pos=[]
for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            shark[board[i][j]] = [i, j, shark_dir[board[i][j]-1]]
            board[i][j] = [board[i][j],k]
        else :
            board[i][j] = [0,0]
keys = list(shark.keys())
keys.sort()
# shark = sorted(shark.items())
# print(shark[2][1][0])
 # dictionary // key : shark_no
dx=[-1,1,0,0]
dy=[0,0,-1,1]
# bfs(board,shark_pos)
# for i in range(n):
#     for j in range(n):
#         if [board[i][j],i,j] in shark_pos:
#             board[i][j] = [board[i][j],k]
#         else:
#             board[i][j] = [0,0]
# bfs(board,shark_pos)
# print(board)
# print('\n')
result = bfs()
print(result)
