#include<stdio.h>
#include<math.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,i,count=1,leaf=0,temp=1,a;
    scanf("%d",&n);

    for(i=0;i<n-1;i++)
    {
    	scanf("%d",&a);

    	if(temp!=a && a<=count)
    	{
    		temp=a;
    		leaf=leaf-1;
    		if(leaf<3)
    		{
    			break;
    		}
    		else
    		{
    			leaf=1;
    		}
    	}
    	else
    	{
    		leaf++;
    	}

    	count++;
    }
    printf("%d\n",leaf );

    if(count==n && leaf>=3)
    {
    	printf("YES\n");
    }
    else
    {
    	printf("NO\n");
    }


}