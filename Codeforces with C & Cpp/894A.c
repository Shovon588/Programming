#include<stdio.h>
#include<string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    char str[100];
    int a,i,j,k,count=0;
    scanf("%s",str);
    a=strlen(str);

    for(i=0;i<a;i++)
    {
    	for(j=i+1;j<a;j++)
    	{
    		for(k=j+1;k<a;k++)
    		{
    			if(str[i]=='Q' && str[j]=='A' && str[k]=='Q')
    			{
    				count++;
    			}
    		}
    	}
    }

    printf("%d\n",count );

}