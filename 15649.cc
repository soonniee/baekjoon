#include <iostream>
using namespace std;
bool used[10]; int choose[10];
void go(int index, int n, int m){
    if(index == m){
        for(int i=0; i<m; i++){
            cout << choose[i];
            if(i != m-1) cout << ' ';
        }
        cout << '\n';
        return;
    }
    for(int i=1; i <=n; i++){
        if(used[i]) continue;
        used[i] = true; choose[index] = i;
        cout << 'a';
        go(index+1,n,m);
        used[i] = false;
        for(int i=1;i<=n;i++) cout << used[i];
    }
}
int main(){
    int n,m;
    cin >> n >> m;
    go(0,n,m);
    return 0;
}