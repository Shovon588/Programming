#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

long long int n,i,count,suma=0,sumb=0,sumc=0;
scanf("%lld",&n);
long long int a[n],b[n-1],c[n-2],j;

for (i=0;i<n;i++)
{
	scanf("%lld",&a[i]);
	suma=suma+a[i];
}
for (i=0;i<n-1;i++)
{
	scanf("%lld",&b[i]);
	sumb=sumb+b[i];
}
for (i=0;i<n-2;i++)
{
	scanf("%lld",&c[i]);
	sumc=sumc+c[i];
}

printf("%lld\n%lld\n",suma-sumb,sumb-sumc );



}