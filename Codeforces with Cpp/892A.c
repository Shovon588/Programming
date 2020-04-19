#include<stdio.h>
#include<string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    long long int n,i,j,c=0,d=0;
    scanf("%lld",&n);
    long long int a[n],b[n],rem=0,cap=0,temp;

    for(i=0;i<n;i++)
    {
    	scanf("%lld",&a[i]);
    	rem=rem+a[i];
    }

    for(i=0;i<n;i++)
    {
    	scanf("%lld",&b[i]);

    	if(b[i]>c)
    	{
    		d=c;
    		c=b[i];
    	}
    	else if(b[i]<=c && b[i]>d)
    	{
    		d=b[i];
    	}
    }


    if((c+d)>=rem)
    {
    	printf("YES\n");
    }
    else
    {
    	printf("NO\n");
    }

}