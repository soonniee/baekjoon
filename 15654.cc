#include <iostream>
#include<algorithm>
using namespace std;
bool used[10]; int num[10]; int choose[10];
void go(int index,int n, int m){
    if(index == m){
        for(int i=0; i<m; i++){
            cout << num[choose[i]];
            if(i != m-1) cout << ' ';
        }
        cout << '\n';
        return;
    }
    for(int i=0; i<n ;i++){
        if(used[i]) continue;
        used[i] = true; choose[index] = i;
        go(index+1,n,m);
        used[i] = false; 
        

    }
}
int main(){
    int n,m;
    cin >> n >> m;
    for(int i=0; i<n ;i++){
        cin >> num[i];
    }
    sort(num,num+n);
    go(0,n,m);
}