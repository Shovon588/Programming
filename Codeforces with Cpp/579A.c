#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

long long int n,count=0;
scanf("%lld",&n);

while(n!=0)
{
	if(n%2==0)
	{
		n=n/2;
	}
	else
	{
		n=n-1;
		count++;
	}
}
printf("%lld\n",count );

}