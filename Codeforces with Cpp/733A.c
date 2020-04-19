#include<stdio.h>
#include<string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    char str[100];
    int i,j,count=1,result=0,a;

    scanf("%s",str);
    a=strlen(str);

    for(i=0;i<a;i++)
    {
    	if(str[i]=='A' || str[i]=='E' || str[i]=='I' || str[i]=='O' || str[i]=='U' || str[i]=='Y')
    	{
    		if(count>result)
    		{
    			result=count;
    		}
    		count=1;
    	}
    	else
    	{
    		count++;
    		if(count>result)
    		{
    			result=count;
    		}
    	}
    }

    printf("%d\n",result );

}