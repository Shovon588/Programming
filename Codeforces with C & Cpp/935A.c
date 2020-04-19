#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    
    int n,i,count=0;
    scanf("%d",&n);

    for(i=1;i<=n/2;i++)
    {
    	if(n%i==0)
    	{
    		count++;
    	}
    }

    printf("%d\n",count );

}