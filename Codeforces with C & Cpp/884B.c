#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

long long int n,x,a,s=0,i;
scanf("%lld%lld",&n,&x);
for(i=0;i<n;i++)
{
	scanf("%lld",&a);
	s=s+a;
}

s=s+n-1;

if(s==x)
{
	printf("YES\n");
}
else
{
	printf("NO\n");
}

}