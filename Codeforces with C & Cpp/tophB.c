#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif


    int n,m,i,a,sum=0,apple;
    scanf("%d%d",&n,&m);

    for(i=0;i<n;i++)
    {
    	scanf("%d",&a);
    	sum=sum+a;
    }

    apple=sum/m;

    if(sum%m==0)
    {
    	printf("%d\n",apple );
    }
    else
    {
    	printf("%d\n",apple+1 );
    }

}