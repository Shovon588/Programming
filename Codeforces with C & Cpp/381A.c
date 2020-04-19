#include<bits/stdc++.h>
using namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    
    int n,i,ser=0,dima=0,sum=0,j;

    scanf("%d",&n);

    int a[n],is_i=0,is_j=n-1;

    for(i=0;i<n;i++)
    {
    	scanf("%d",&a[i]);
    }

    for(j=1;j<=n;j++)
    {
    	if(j%2!=0)
    	{
    		if(a[is_i]>=a[is_j])
    		{
    			ser=ser+a[is_i];
    			is_i++;
    		}
    		else
    		{
    			ser=ser+a[is_j];
    			is_j--;
    		}
    	}
    	else
    	{
    		if(a[is_i]>=a[is_j])
    		{
    			dima=dima+a[is_i];
    			is_i++;
    		}
    		else
    		{
    			dima=dima+a[is_j];
    			is_j--;
    		}

    	}

    }

    printf("%d %d\n",ser,dima );

}