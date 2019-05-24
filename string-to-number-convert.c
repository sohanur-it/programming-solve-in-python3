#include <stdio.h>
#include <string.h>


int main()
{
int T;
char str[100];
printf("ENter the nth value :");
scanf("%d",&T);
for(int j=1;j<=T;j++){
printf("Enter a string :");
scanf("%s",&str);
printf("%s\n",str);
for(int i=0;str[i] != '\0';i++){
if(str[i]>='A' && str[i]<='Z'){
        printf("%d",str[i]-64);
        }

    }
    printf("\n");
}
return 0;
}
