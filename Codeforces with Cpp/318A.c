#include<stdio.h>
#include<string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

	long long int n,k,result;
	scanf("%lld%lld",&n,&k);

	if(k<=(n+1)/2)
	{
		result=(2*k)-1;
	}
	else
	{
		result=2*(k-(n+1)/2);
	}

	printf("%lld\n",result );

}