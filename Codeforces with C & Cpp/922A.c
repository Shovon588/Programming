#include<stdio.h>
#include <string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    long long int n,m,temp;
    scanf("%lld%lld",&n,&m);

    m=m-1;

    temp=n-m;

    if(n==0 || m==0)
    {
        printf("No\n");
    }

    else if(temp%2==0)
    {
    	printf("Yes\n");
    }
    else
    {
    	printf("No\n");
    }

}