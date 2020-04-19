#include<stdio.h>
#include <string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

int n,i,price,quality,count=0;
scanf("%d",&n);
int a[n],b[n];

for(i=0;i<n;i++)
{
	scanf("%d%d",&a[i],&b[i]);
}
price=a[0];
quality=b[0];

for (i=0;i<n;i++)
{
	if(price>quality)
	{
		if(a[i]<b[i])
		{
			printf("Happy Alex\n");
			break;
		}
		else
		{
			count++;
		}
	}
	else if(price<quality)
	{
		if(a[i]>b[i])
		{
			printf("Happy Alex\n");
			break;
		}
		else
		{
			count++;
		}
	}
	else
	{
		if(a[i]!=b[i])
		{
			price=a[i];
			quality=b[i];
			count++;
		}
		else
		{
			count++;
		}
	}
}

if(count==n)
{
	printf("Poor Alex\n");
}
}