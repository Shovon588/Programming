#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,m,p,s,i,j,count=0;
    scanf("%d%d",&n,&m);
    int a[105]={0};

    for(i=0;i<n;i++)
    {
    	scanf("%d",&p);
    	for(j=0;j<p;j++)
    	{
    		scanf("%d",&s);
    		a[s-1]++;
    	}
    }

    for(i=0;i<m;i++)
    {
    	if(a[i]==0)
    	{
    		printf("NO\n");
    		break;
    	}
    	else
    	{
    		count++;
    	}
    }

    if(count==m)
    {
    	printf("YES\n");
    }
}