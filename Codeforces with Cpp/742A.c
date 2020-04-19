#include<stdio.h>
#include<string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    long long int n;
    scanf("%lld",&n);
    int a[4]={6,8,4,2};
	
	if(n==0)
	{
		printf("1\n");
	}
	else
	{
		printf("%d\n",a[n%4] );
	}


}