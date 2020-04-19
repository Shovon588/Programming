#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

long long int a[4];
int i,j,count=0;
for(i=0;i<4;i++)
{
scanf("%lld",&a[i]);
}
for(i=0;i<4;i++)
{
for(j=0;j<i;j++)
{
if(a[i]==a[j])
{
count++;
break;
}
}
}

printf("%d",count);
return 0;
}