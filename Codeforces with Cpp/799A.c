#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

int n,t,k,d,temp,i;
scanf("%d%d%d%d",&n,&t,&k,&d);
i=0;

while(temp<d)
{
	i++;
	temp=(i*t);
}

if(temp==d)
{
	if(n-(i*k)>k)
	{
		printf("YES\n");
	}
	else
	{
		printf("NO\n");
	}
}
else
{
	if(n-(i*k)>0)
	{
		printf("YES\n");
	}
	else
	{
		printf("NO\n");
	}
}


}