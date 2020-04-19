#include<stdio.h>
#include <string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

int k,w,temp,i;
long long int n,cost=0,result;
scanf("%d%lld%d",&k,&n,&w);

for(i=1;i<=w;i++)
{
temp=i*k;
cost=cost+temp;
}
result=cost-n;

if(result<0)
{
printf("0\n");
}
else
{
printf("%lld\n",result);
}



}