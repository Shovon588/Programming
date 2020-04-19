#include<stdio.h>
#include<string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,k,i,time,count=0,j=1;

    scanf("%d%d",&n,&k);
    

    time=240-k;

    i=1;

    while(i*5<=time && j<=n)
    {
    	time=time-(i*5);
    	i++;
    	count++;
    	j++;
    }

    printf("%d\n",count );
}