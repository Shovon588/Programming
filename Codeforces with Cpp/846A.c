#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

int n,i,count=0;
scanf("%d",&n);
int a[n];

for(i=0;i<n;i++)
{
	scanf("%d",&a[i]);
}

for(i=0;i<n;i++)
{
	if(a[i]==1 && a[i+1]==0)
	{
		continue;
	}
	else
	{
		count++;
	}
}
printf("%d\n",count );


}