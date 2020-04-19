#include<stdio.h>
#include <string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

int m,n,sum,div;
scanf("%d%d",&m,&n);
sum=m*n;
div=sum/2;
printf("%d\n",div);



}