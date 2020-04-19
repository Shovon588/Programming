#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    
    int n,x,co=0,i=0;

    scanf("%d",&n);


    for(i=1;i<=n;i++)
    {
        x=n-i;
       printf("%d--%d--%d\n",x,i,co );
        if(x%i==0)
        {
            co++;
        }

       
    }

    printf("%d\n",co-1 );
}