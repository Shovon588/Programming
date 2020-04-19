#include<stdio.h>
#include <string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

int n,a[3],i,j,result=0;
scanf("%d",&n);

for(i=0;i<n;i++)
{
int count=0;
for(j=0;j<3;j++)
{
scanf("%d",&a[j]);

if(a[j]==1)
{
count++;
}
}
if(count>=2)
{result++;}
}

printf("%d\n",result);
}