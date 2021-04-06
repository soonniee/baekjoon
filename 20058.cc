#include<iostream>
#include<algorithm>
#include<vector>
#include<cmath>
using namespace std;
int N, Q;
int a[65][65];
int L[1001];
int map_size;
int ice_count = 0;
int dx[]={-1,1,0,0};
int dy[]={0,0,-1,1};
typedef struct coord{
    int x;
    int y;
}C;
vector<C> ice_minus;
int sum_ice = 0; 
int max_ice = 0;
int vis[65][65];
void rotate(int storm_size,int divide_row,int num){
    int row = num / divide_row;
    num %= divide_row;
    int temp[storm_size][storm_size];
    int row_size = (row+1)*storm_size;
    int col_size = (num+1)*storm_size;
    row = row * storm_size;
    int col = num * storm_size;
    printf("row:%d %d  col:%d %d \n",row,row_size,col,col_size);
    int temp_row = 0;
    int temp_col = 0;
    for(int i=col;i<col_size;i++){
        for(int j=row_size-1;j>=row;j--){
            temp[temp_row][temp_col] = a[j][i];
            temp_col++;
        }
        temp_row++;
        temp_col = 0;
    }
    temp_row = 0;
    temp_col = 0;
    for(int i=row;i<row_size;i++){
        for(int j=(col);j<col_size;j++){
            a[i][j] = temp[temp_row][temp_col];
            temp_col++;
        }
        temp_row++;
        temp_col = 0;
    }
}
void check_ice(){
    ice_minus.clear();
    for(int i=0;i<map_size;i++){
        for(int j=0;j<map_size;j++){
            if(a[i][j]>0){
                if(i==0 && j == 0) {
                    ice_minus.push_back({i,j}); 
                }
                else if(i==0 && j == map_size-1) {
                    ice_minus.push_back({i,j}); 
                }
                else if(i==map_size-1 && j == 0) {
                    ice_minus.push_back({i,j}); 
                }
                else if(i==map_size-1 && j == map_size-1) {
                    ice_minus.push_back({i,j}); 
                }
                else{
                    int ck = 0;
                    for(int k=0;k<4;k++){
                        
                        int nx = i + dx[k];
                        int ny = j + dy[k];
                        if(nx<0 || nx >=map_size || ny<0 || ny >= map_size){
                            ck++;
                            
                        }
                        else{
                            if(a[nx][ny]==0){
                                ck++;   
                            }
                        }
                        
                    }
                    if(ck>1) ice_minus.push_back({i,j});
                        
                }
            }
            
            
        }
    }
    for(int i=0;i<ice_minus.size();i++){
        a[ice_minus[i].x][ice_minus[i].y] -=1;
    }
}
void firestorm(int storm_size){
    int divide_row = map_size / storm_size;
   int divide_num = pow(divide_row,2);
   for(int i=0;i<divide_num;i++){
       rotate(storm_size,divide_row,i);
   }
   check_ice();
   
   for(int i=0;i<map_size;i++){
        for(int j=0;j<map_size;j++){
            printf("%d\t",a[i][j]);
        }
        printf("\n");
    }
}
void dfs(int x,int y){
    for(int i=0;i<4;i++){
        int nx = x + dx[i];
        int ny = y + dy[i];
        if(nx<0||nx>=map_size || ny<0 || ny>=map_size) continue;
        if(vis[nx][ny]||a[nx][ny]<=0) continue;
        vis[nx][ny] = 1;
        dfs(nx,ny);
        ice_count++;
    }
}
void simulation(){
    for(int i=0;i<Q;i++){
        int storm_size = pow(2,L[i]);
        firestorm(storm_size);
    }
     for(int i=0;i<map_size;i++){
        for(int j=0;j<map_size;j++){
            printf("%d\t",a[i][j]);
        }
        printf("\n");
    }
    int ans = 0;
    for(int i=0;i<map_size;i++){
        for(int j=0;j<map_size;j++){
            sum_ice+=a[i][j];
            ice_count = 0;
            // vis[i][j]=1;
            dfs(i,j);
            if(ans<ice_count) ans=ice_count;
            printf("%d\n",ans);
        }
    }
    cout << sum_ice <<'\n' << ans;
}



int main(){
    cin >> N >> Q;
    map_size = pow(2,N);
    for(int i=0;i<map_size;i++){
        for(int j=0;j<map_size;j++){
            cin >> a[i][j];
        }
    }
    for(int i=0;i<Q;i++) cin >> L[i];
    simulation();
}