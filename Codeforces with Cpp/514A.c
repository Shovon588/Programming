#include<stdio.h>
#include<string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    char str[10];
    int i,n;
    scanf("%s",str);
    n=strlen(str);

    for(i=0;i<n;i++)
    {
    	if(str[i]>='5' && str[i]<='9')
    	{
    		if(str[i]=='9' && i==0)
    		{
    			continue;
    		}
    		else
    		{
    			str[i]='9'-str[i]+'0';
    		}
    	}
    }

    printf("%s\n",str );


}