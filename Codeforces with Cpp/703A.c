#include<stdio.h>
int main()
{
    int n,a,b,miska=0,chris=0,i;
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        scanf("%d%d",&a,&b);
        if(a>b){miska++;}
        else if(a<b){chris++;}
    }
    if(miska==chris){printf("Friendship is magic!^^");}
    else if(miska>chris){printf("Mishka");}
    else{printf("Chris");}


    return 0;
}
