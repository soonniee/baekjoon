#include<iostream>
#include<algorithm>
using namespace std;
int n,m,k;
typedef struct FireBall{
    int x;
    int y;
    int mass;
    int dir;
    int speed;
} FB;
FB F[2501];
void init_map(){
    int map[n][n];
    for(int i=0;i<m;i++){
        int x = F[i].x;
        int y = F[i].y;
        map[x][y] = i;
    }
}
int main(){
    cin >> n >> m >> k;
    for(int i=0;i<m;i++){
        for(int j=0;j<5;j++){
            cin >> F[i].x >> F[i].y >> F[i].mass >> F[i].dir >> F[i].speed;
        }
    }
    init_map(n,m);
    return 0;
}