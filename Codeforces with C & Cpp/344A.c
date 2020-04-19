#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

long long int n;
scanf("%lld",&n);
int a[n],i,count=0;

for(i=0;i<n;i++)
{
scanf("%d",&a[i]);
}

for(i=0;i<n-1;i++)
{
if(a[i]!=a[i+1])
{
count++;
}
}
printf("%d",count+1);


return 0;
}