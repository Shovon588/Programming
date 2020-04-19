#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif


    int n,m,i,temp,x;
    scanf("%d%d",&n,&m);
    int a[n],b[m];

    for(i=0;i<n;i++)
    {
    	scanf("%d%d",&a[i],&b[i]);
    }

    x=b[0];

    for(i=1;i<n;i++)
    {
    	if(x>=a[i])
    	{
    		if(b[i]>x)
    		{
    			x=b[i];
    		}
    		else
    		{
    			break;
    		}
    	}
    }


    if(x>=m)
    {
    	printf("YES\n");
    }
    else
    {
    	printf("NO\n");
    }

}