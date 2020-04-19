#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

int a[3],b[3],n,i,counta=0,countb=0,tempa,tempb;
for(i=0;i<3;i++)
{
	scanf("%d",&a[i]);
	counta=counta+a[i];
}
for(i=0;i<3;i++)
{
	scanf("%d",&b[i]);
	countb=countb+b[i];
}
scanf("%d",&n);
if(counta%5==0)
{
	tempa=counta/5;
}
else
{
	tempa=(counta/5)+1;
}

if(countb%10==0)
{
	tempb=countb/10;
}
else
{
	tempb=(countb/10)+1;
}

if(tempa+tempb<=n)
{
	printf("YES\n");
}
else
{
	printf("NO\n");
}



}