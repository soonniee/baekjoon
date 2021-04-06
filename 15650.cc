#include <iostream>
using namespace std;
bool used[10]; int choose[10];
void go(int index, int start, int n, int m){
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
        
        go(index+1,i+1,n,m);
        used[i] = false;
       
    }
}
int main(){
    int n,m;
    cin >> n >> m;
    go(0,1,n,m);
    return 0;
}