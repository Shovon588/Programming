#include<stdio.h>
#include<string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    char str[100];
    scanf("%s",str);
    int i,a,count=0,j=0,k;
    a=strlen(str);

    for(i=0;i<a;i++)
    {
    	if((str[i]=='A' && str[i+1]=='B') || (str[i]=='B' && str[i+1]=='A'))
    	{
    		if(str[i]=='A')
    		{
    			j=1;
    		}
			i=i+2;
   			count++;
   			break;
   		}	
    }


    if(j==1)
    {
    	for(k=i;k<a;k++)
    	{

    		if(str[k]=='B' && str[k+1]=='A')
    		{
    			count++;
    			break;
    		}
    	}
    }
    else
    {
    	for(k=i;k<a;k++)
    	{
    		if(str[k]=='A' && str[k+1]=='B')
    		{
    			count++;
    			break;
    		}
    	}
    }

    if(count==2)
    {
    	printf("YES\n");
    }
    else
    {
    	printf("NO\n");
    }

}