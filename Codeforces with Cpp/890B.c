#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,i,j,ans=10;
    scanf("%d",&n);
    int a[n];
    for(i=0;i<n;i++)
    {
    	scanf("%d",&a[i]);
    }


    for(i=0;i<n;i++)
    {
    	for(j=1;j<n;j++)
    	{
    		if(a[i]==a[j])
    		{
    			if(j<ans)
    			{
    			ans=j;
    			}
    		}
    	}
    	printf("%d\n",ans );
    }
    	

printf("%d\n",a[ans-1] );
}