#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,sum=0;
    scanf("%d",&n);
    char str[100],z;

    for(int i=0;i<n;i++)
    {
    	scanf("%s",str);

    	if(str[0]=='T')
    	{
    		sum=sum+4;
    	}
    	else if(str[0]=='C')
    	{
    		sum=sum+6;
    	}
    	else if(str[0]=='O')
    	{
    		sum=sum+8;
    	}
    	else if(str[0]=='D')
    	{
    		sum=sum+12;
    	}
    	else if(str[0]=='I')
    	{
    		sum=sum+20;
    	}
    }

    printf("%d\n",sum );

}