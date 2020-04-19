#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

int socks,m,i,count=0,b;
scanf("%d%d",&socks,&m);
b=2*socks;

for(i=1;i<=b;i++)
{
if(i%m==0)
{
socks=socks;
count++;
}

else
{
socks=socks-1;
count++;
}

if(socks==0)
{
printf("%d",count);
break;
}

}


return 0;
}