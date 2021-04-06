from copy import deepcopy
def dfs(x,y,d,cnt):
    global ans,graph,fish

    # print("graph")


    fish_move()
    print(graph)
    copy_graph, copy_fish = deepcopy(graph), deepcopy(fish)
    if ans < cnt :
        ans = cnt

    for  i in range(1,4):

        nx = x + dx[d-1]*i
        ny = y + dy[d-1]*i
        print(i,nx,ny)
        if(nx < 0 or nx >= 4 or ny < 0 or ny >= 4):
            print("return")
            return
        else:
            if not graph[nx][ny]:
                print("cont")
                continue
            else:


                copy_graph[x][y] = []
                tmp = copy_graph[nx][ny][0]

                print(copy_graph[nx][ny][0],cnt)
                copy_fish[copy_graph[nx][ny][0]]=[]
                copy_graph[nx][ny]=[-1, copy_graph[nx][ny][1]]
                # print(nx,ny)
                # cnt = cnt + copy_graph[nx][ny][0]
                print("dfs")
                print(copy_graph)



                graph, fish = deepcopy(copy_graph), deepcopy(copy_fish)
                dfs(nx,ny,copy_graph[nx][ny][1],cnt+tmp)
                # copy_graph[x][y] = [-1,copy_graph[nx][ny][1]]

                # print(copy_fish)
        print("after dfs")
                # graph, fish = copy_graph, copy_fish
                # print(fish)
                # fish[graph[nx][ny][0]]
                # graph, fish = deepcopy(copy_graph), deepcopy(copy_fish)
                # graph, fish = copy_graph, copy_fish

            # print(1)


def fish_move():

    for i in range(0,17):
        if fish[i]:

            x = fish[i][0]
            y = fish[i][1]


            index = graph[x][y][1]-1
            for j in range(8):
                index = (index + j) % 8
                nx = x + dx[index]
                ny = y + dy[index]
                if( 0 <= nx < 4 and 0 <= ny < 4):

                    if(graph[x][y][0]!=-1 and graph[nx][ny][0]!=-1):
                        fish[graph[nx][ny][0]]=[x,y]
                        fish[i]=[nx,ny]
                        graph[nx][ny] , graph[x][y] = graph[x][y], graph[nx][ny]
                        
                        break



graph=[[] for _ in range(4)]
fish = [[]for _ in range(17)]
for i in range(4):
    temp = list(map(int,input().split()))
    for j in range(0,7,2):
        graph[i].append([temp[j],temp[j+1]])
        fish[temp[j]] = [i,j //2]
dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,-1,-1,-1,0,1,1,1]

# sx = 0
# sy = 0
ans=0
d = graph[0][0][1]
cnt = graph[0][0][0]
fish[cnt]=[]
graph[0][0][0]=-1
dfs(0,0,d,cnt)
print(ans)
# print(graph)
