#include<stdio.h>
#include <string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif


int n,i,even=0,a[100];
scanf("%d",&n);
for(i=0;i<n;i++)
{
scanf("%d",&a[i]);
if(a[i]%2==0)
{
even=even+1;
}
}
if(even==1)
{
for(i=0;i<n;i++)
{
if(a[i]%2==0)
{
printf("%d",i+1);
}
}
}
else
{
for(i=0;i<n;i++)
{
if(a[i]%2!=0)
{
printf("%d",i+1);
}
}
}



return 0;
}