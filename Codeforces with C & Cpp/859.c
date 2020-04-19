#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

	long long int n,m,a,count=0;

	scanf("%lld%lld%lld",&n,&m,&a);

	if(n<=a && m<=a)
	{
		if
	}

	if(n%a==0)
	{
		count=count+(n/a);
	}
	else
	{
		count=count+(n/a)+1;
	}

	if(m%a==0)
	{
		count=count+(m/a);
	}
	else
	{
		count=count+(m/a)+1;
	}

	printf("%lld\n",count );



}