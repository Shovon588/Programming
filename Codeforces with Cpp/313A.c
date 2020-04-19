#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

long long int n,temp,a,b,temp2;
scanf("%lld",&n);
temp=n;

a=temp/10;
temp2=temp%10;

b=(a/10)*10+temp2;
if(a>=b)
{
	if(a>n)
	{
		printf("%lld\n",a );
	}
	else
	{
		printf("%lld\n",n );
	}
}
else if(b>a)
{
	if(b>n)
	{
		printf("%lld\n",b );
	}
	else
	{
		printf("%lld\n",n );
	}
}


}