#include<stdio.h>
#include <string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

int n,i,checkx=0,checky=0,checkz=0;
scanf("%d",&n);
int x[n],y[n],z[n];
for(i=0;i<n;i++)
{
scanf("%d%d%d",&x[i],&y[i],&z[i]);
}
for(i=0;i<n;i++)
{
checkx=checkx+x[i];
}
for(i=0;i<n;i++)
{
checky=checky+y[i];
}
for(i=0;i<n;i++)
{
checkz=checkz+z[i];
}

if(checkx==0 && checky==0 && checkz==0)
{
printf("YES\n");
}
else
{
printf("NO\n");
}


}