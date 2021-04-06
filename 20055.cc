#include <iostream>
#include <algorithm>
#include <stdio.h>
using namespace std;
int n,k;
typedef struct belt{
    int robot;
    int strong;
    int move;
}Belt;
Belt B[201];
int main(){
    cin >> n >> k;
    
    for(int i=0;i<2*n;i++){
        B[i].robot = 0;
        B[i].move = 0;
        cin >> B[i].strong;
        printf("%d\n" ,B[i].strong);
    }
    printf("%d %d",n,k);
    int cnt = 0;
    printf("%d",cnt);
    while(1){
        if(B[0].robot == 0 && B[0].strong > 0){
            B[0].robot = 1;
            B[0].strong -=1;
            break;
        }
        else{
            for(int i=2*n-1 ;i>0;i--){
                B[i] = B[i-1];
            }
            B[0].strong = B[2*n-1].strong;
        }
        cnt++;
        printf("%d",cnt);
    }
    printf("%d",cnt);
    // B[0].strong -=1;
    // B[0].robot = 1;
    // int cnt = 0;
    while(1){
        if(B[0].robot == 0 && B[0].strong > 0){
            B[0].robot = 1;
            B[0].strong -=1;
        }
        if(B[2*n-1].robot == 1) B[2*n-1].robot = 0;
        for(int i=2*n-1 ;i>0;i--){
            B[i].strong = B[i-1].strong;
        }
        B[0].strong = B[2*n-1].strong;
        
        
        for(int i=0;i<2*n-1;i++){
            if(B[i].robot ==1){
                if(B[i+1].robot == 0 && B[i+1].strong > 0){
                    B[i+1].move = 1;
                }
            }
        }
        for(int i=0;i<2*n;i++){
            if(B[i].move ==1 ){
                B[i].robot = 1;
                B[i].strong -=1;
                B[i].move = 0;
            }
        }
        int strong_cnt =0;
        for(int i=0;i<2*n;i++){
            if(B[i].strong==0) strong_cnt++;
        }
        if(strong_cnt >= k) break;
        else cnt++;
    }
    cout << cnt;
    
}