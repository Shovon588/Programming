#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    long long int n,k,lcount=0,scount=0,i=1;
    scanf("%lld%lld",&n,&k);

    if((n/k)%2==0)
    {
    	printf("NO\n");
    }
    else
    {
    	printf("YES\n");
    }
}