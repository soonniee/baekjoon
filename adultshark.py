
def bfs(board,shark_pos):
    time = 0
    shark_num = len(shark_pos)

    # smell = [[] for _ in range(k)]

    while(1):
        # print("dsfasd")
        crash_shark = []
        queue = []
        visited = []

        time = time + 1
        for index in shark_pos:
            flag_blank = 0

            shark_no = index[0]-1
            x = index[1]
            y = index[2]
            dir = shark_dir[shark_no]
            move_rank = dir_rank[shark_no * 4 + dir - 1]
            for d in move_rank:
                nx, ny = x + dx[d-1], y + dy[d-1]
                if(0 <= nx < n and 0 <= ny < n):
                    if(board[nx][ny] == [0,0]):
                        # board[x][y]
                        if [nx,ny] in visited:
                            crash_shark.append(shark_no)
                        else :
                            visited.append([nx,ny])
                            queue.append([shark_no + 1,nx,ny])
                            shark_dir[shark_no] = d
                        flag_blank = 1
                        break
            if(flag_blank == 0):
                flag_smell = 0
                for d in move_rank:
                    nx, ny = x + dx[d-1], y + dy[d-1]
                    if(0 <= nx < n and 0 <= ny < n):
                        if(board[nx][ny][0] == shark_no + 1):
                            flag_smell = 1
                            # if [nx,ny] in visited:
                            #     crash_shark.append(shark_no)
                            # else :
                                # visited.append([nx,ny])
                            queue.append([shark_no + 1,nx,ny])
                            shark_dir[shark_no] = d
                            break
                if flag_smell == 0 :
                    crash_shark.append(shark_no)


        for i in range(n):
            for j in range(n):
                if board[i][j][0] != 0 :
                    board[i][j][1] -= 1
                    if(board[i][j][1] == 0):
                        board[i][j] =[0,0]
        for a in queue:
            board[a[1]][a[2]] = [a[0],k]
            for i in range(len(shark_pos)):
                if shark_pos[i][0] == a[0]:
                    shark_pos[i] = [a[0],a[1],a[2]]
        for c in crash_shark:
            for i in range(len(shark_pos)):
                if shark_pos[i][0] == c+1:
                    del shark_pos[i]
            # shark_pos.pop(c)
        shark_num = len(shark_pos)
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
# print(dir_rank)
shark_pos=[]
for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            shark_pos.append([board[i][j],i,j])
            board[i][j] = [board[i][j],k]
        else :
            board[i][j] = [0,0]
shark_pos = sorted(shark_pos, key = lambda x : x[0])

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
result = bfs(board,shark_pos)
print(result)
