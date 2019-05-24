#include <stdio.h>
#include <stdlib.h>

int main()
{
    int T,N;
    printf("Enter the input numbers : ");
    scanf("%d",&T);
    for(int i=1;i<=T;i++){
    printf("case%d:",i);
    scanf("%d",&N);
    long long int factorial=1,i;
    for(i=2;i<=N;i++){
    factorial=factorial*i;
    }
    printf("factorial=%lld\n",factorial);
    }


    return 0;
}
