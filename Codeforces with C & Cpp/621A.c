#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,i,j,temp,c=0;
    scanf("%d",&n);
    long long int a[n],sum=0,small=1000000000;

    for(i=0;i<n;i++)
    {
    	scanf("%lld",&a[i]);
    	sum=sum+a[i];
    	if(a[i]<small)
    	{
    		small=a[i];
    	}
    }


if(sum%2==0)
{
	printf("%lld\n",sum );
}
else
{
		sum=sum-small;
		if(sum%2==0)
		{
			printf("%lld\n",sum );
		}
	}


}