#include<stdio.h>
#include<string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int t,a,i;
    scanf("%d",&t);

    for(i=0;i<t;i++)
    {
    	scanf("%d",&a);
    	a=180-a;

    	if(360%a==0)
    	{
    		printf("YES\n");
    	}
    	else
    	{
    		printf("NO\n");
    	}
    }

}