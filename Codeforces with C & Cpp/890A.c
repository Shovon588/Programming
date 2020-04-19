#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif


    int i,sum=0,a[6];
    for(i=0;i<6;i++)
    {
    	scanf("%d",&a[i]);
    	sum=sum+a[i];
    }

    printf("%d\n",sum );

    

}