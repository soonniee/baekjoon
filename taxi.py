n,m,k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
start_x, start_y = map(int,input().split())
start_x -= 1
start_y -= 1
passenger = [list(map(int,input().split())) for _ in range(m)]
for i in range(m):
    for j in range(4):
        passenger[i][j] -= 1
# print(board)
# print(passenger)
dx = [-1,0,0,1] # up left right down
dy = [0,-1,1,0]
def find_passenger(taxi_x,taxi_y,taxi_p):
    # global board
    board[taxi_x][taxi_y] = 1
    find_flag = 0
    # gx, gy = p[0], p[1]
    queue = [[taxi_x, taxi_y, 0]]
    visited = [[taxi_x, taxi_y]]
    while queue:
        cnt = -1
        sx,sy,dis = queue.pop(0)
        for p in taxi_p:
            cnt += 1
            if sx == p[0] and sy == p[1]:
                find_flag = 1
                board[taxi_x][taxi_y] = 0
                return cnt,p,dis,find_flag
        for i in range(4):
            nx,ny = sx + dx[i], sy + dy[i]
            if(0 <= nx < n and 0 <= ny < n and [nx,ny] not in visited):
                if(board[nx][ny] != 1):
                    queue.append([nx,ny,dis+1])
                    visited.append([nx,ny])
    if find_flag == 0:
        return 0,0,0,0

def find_arrival(p_x,p_y,arrival_x,arrival_y):
    # min_passenger, dis = find_passenger()
    board[p_x][p_y] = 1
    queue = [[p_x, p_y, 0]]
    visited = [[p_x, p_y]]
    find_flag = 0
    while queue:
        # print(queue)
        sx,sy,dis = queue.pop(0)

        if sx == arrival_x and sy == arrival_y:
            find_flag = 1
            board[p_x][p_y] = 0
            return dis,find_flag
        for i in range(4):
            nx,ny = sx + dx[i], sy + dy[i]
            if(0 <= nx < n and 0 <= ny < n and [nx,ny] not in visited):
                if(board[nx][ny] != 1):
                    queue.append([nx,ny,dis+1])
                    visited.append([nx,ny])
    if find_flag == 0:
        return 0,0
    # while queue:

def bfs(x,y,p):
    fuel = k
    # a,b=find_passenger(x,y)
    # print(board)
    while(fuel > 0):
        # print(fuel)
        # print(p)
        passenger_no,min_passenger,dis_p,flag_p = find_passenger(x,y,p)
        # print(flag_p)
        if(dis_p >= fuel or flag_p == 0):
            return -1

        fuel = fuel - dis_p
        dis_a,flag_a = find_arrival(min_passenger[0],min_passenger[1],min_passenger[2],min_passenger[3])
        # print(flag_p)
        if(dis_a > fuel or flag_a == 0):
            return -1

        fuel = fuel + dis_a
        x,y = min_passenger[2], min_passenger[3]
        del passenger[passenger_no]
        p = passenger
        if len(p) == 0 :
            return fuel
    # print(min_passenger)
    # print(dis)
result= bfs(start_x,start_y,passenger)
print(result)
