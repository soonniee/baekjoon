#include <iostream>
using namespace std;
int a[10][10];
bool visited[10][10];
int n,m,k;
int ans = -2148483647;
int dx[]={0,0,1,-1};
int dy[]={1,-1,0,0};
void go(int prev, int cnt, int sum){
    if(cnt == k){
        if(ans < sum) ans = sum;
        return;
    }
    for(int i=prev+1; i<n*m; i++){
        int x = i/m;
        int y = i%m;
        if(visited[x][y]) continue;
        bool ok = true;
        for(int j=0;j<4;j++){
            int nx = x + dx[j]
            int ny = y + dy[j]
            if(0<=nx && nx < n && 0<=ny && ny<m){
                if(visited[nx][ny]) ok = false;
            }
            if(ok){
                visited[x][y] = true;
                go(x*m+y, cnt+1, sum+a[x][y]);
                visited[x][y] = false;
            }
        }
    }
}
int main(){
    cin >> n >> m >> k;
    for(int i=0; i<n ;i++){
        for(int j=0; j<m; j++){
            cin >> a[i][j];
        }
    }
    go(-1,0,0);
}