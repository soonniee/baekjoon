from collections import deque
import sys
ger(taxi_x,taxi_y,passenger):
    # global board
    # if passenger.get()
    global fuel
    board[taxi_x][taxi_y] = 1
    find_flag = 0
    # gx, gy = p[0], p[1]
    queue = deque()
    queue.append([taxi_x,taxi_y,0])
    visited = [[taxi_x, taxi_y]]
    while queue:
        # cnt = -1
        sx,sy,cnt = queue.popleft()

        if cnt >= (fuel-1) :
            # print("dasfadfsd")
            return -1
        for i in range(4):
            nx,ny = sx + dx[i], sy + dy[i]
            if(0 <= nx < n and 0 <= ny < n and [nx,ny] not in visited):
                if(board[nx][ny] != 1):
                    if board[nx][ny] == -1:
                        board[taxi_x][taxi_y] = 0
                        board[nx][ny] = 0
                        find_flag = 1
                        fuel = fuel - (cnt + 1)
                        return nx,ny
                    else :
                        queue.append([nx,ny,cnt+1])
                        visited.append([nx,ny])
    if find_flag == 0:
        return -1

def find_arrival(p_x,p_y):
    global fuel
    # min_passenger, dis = find_passenger()
    board[p_x][p_y] = 1
    queue = deque()
    queue.append([p_x, p_y,0])
    visited = [[p_x, p_y]]
    find_flag = 0
    while queue:
        # print(queue)
        sx,sy,cnt = queue.popleft()
        if cnt >= fuel :
            return -1
        for i in range(4):
            nx,ny = sx + dx[i], sy + dy[i]
            if(0 <= nx < n and 0 <= ny < n and [nx,ny] not in visited):
                if(board[nx][ny] != 1):
                    if nx == passenger[(p_x,p_y)][0] and ny == passenger[(p_x,p_y)][1]:
                        find_flag = 1
                        board[p_x][p_y] = 0
                        board[nx][ny] = 0
                        fuel = fuel + (cnt+1)
                        return 0
                    else :
                        queue.append([nx,ny,cnt+1])
                        visited.append([nx,ny])
    if find_flag == 0:
        return -1

    # while queue:

def bfs(x,y,passenger):
    # a,b=find_passenger(x,y)
    # print(board)
    global fuel
    while 1:
        #print(fuel)
        # print(p)
        res = find_passenger(x,y,passenger)
        # print(res)
        if(res == -1):
            print(-1)
            break
        sx,sy = res
        # print(fuel)
        res1 = find_arrival(sx,sy)
        # print(res1)
        # print(flag_p)
        if(res1 == -1):
            print(-1)
            break
        x,y = passenger[(sx,sy)][0], passenger[(sx,sy)][1]
        del passenger[(sx,sy)]
        # p = passenger
        if not passenger:
            print(fuel)
            break
    # print(min_passenger)
    # print(dis)
n,m,fuel = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
start_x, start_y = map(int,sys.stdin.readline().split())
start_x -= 1
start_y -= 1
# passenger = [list(map(int,input().split())) for _ in range(m)]
passenger={}
for _ in range(m):
    x,y,x1,y1 = map(int,sys.stdin.readline().split())
    passenger[(x - 1, y - 1)] = [x1 - 1, y1 - 1]
    board[x-1][y-1] = -1

# print(board)
# print(passenger)
dx = [-1,0,0,1] # up left right down
dy = [0,-1,1,0]
def find_passen
bfs(start_x,start_y,passenger)
