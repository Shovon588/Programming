#include<stdio.h>
#include<string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int a,i,n,j,count=0,unique;

    scanf("%d",&n);

    char str[100];

    scanf("%s",str);
   
    for(i=0;i<n;i++)
    {
    	if(str[i]>=65 && str[i]<=90)
    	{
    		str[i]=str[i]+32;
    	}
    }

    for(i=0;i<n;i++)
    {
    	for(j=i+1;j<n;j++)
    	{
    		if(str[i]==str[j])
    		{
    			count++;
    			break;
    		}
    	}
    }

    unique=n-count;

    if(unique==26)
    {
    	printf("YES\n");
    }
    else
    {
    	printf("NO\n");
    }



}