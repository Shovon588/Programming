#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    
    long long int n,a;

    scanf("%lld",&n);

    a=n%10;

    if(a==0)
    {
    	printf("%lld\n",n );
    }
    else if(a>=5)
    {
    	printf("%lld\n",n+(10-a) );
    }
    else
    {
    	printf("%lld\n",n-a );
    }


}