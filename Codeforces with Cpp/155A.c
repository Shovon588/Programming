#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

int n,i,low,high,count=0;
scanf("%d",&n);
int a[n];

for(i=0;i<n;i++)
{
	scanf("%d",&a[i]);
}
low=a[0];
high=a[0];

for(i=0;i<n;i++)
{
	if(a[i]>high)
	{
		count++;
		high=a[i];
	}
	else if(a[i]<low)
	{
		count++;
		low=a[i];
	}
}
printf("%d\n",count );


}