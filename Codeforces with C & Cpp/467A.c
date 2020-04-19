#include<stdio.h>
#include <string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

int n,a,b,i,check,count=0;
scanf("%d",&n);
for(i=0;i<n;i++)
{
scanf("%d%d",&a,&b);
check=b-a;
if(check>=2)
{
count++;
}
}
printf("%d\n",count);


}