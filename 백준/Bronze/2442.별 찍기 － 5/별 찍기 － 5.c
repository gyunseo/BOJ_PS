#include<stdio.h>

int main(){
    
    int n;
    int i,j;
    scanf("%d",&n);
    
    
      for(i=1;i<=n;i++){
        
        for(j=1;j<=(n+i-1);j++){
            if(j<=(n-i)) printf(" ");
            else printf("*");
        }
          
        printf("\n");
    }
    
    return 0;
    
}