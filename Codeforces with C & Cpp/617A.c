#include<stdio.h>
#include <string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

int n,count=0;
scanf("%d",&n);
count=count+(n/5);
n=n%5;
count=count+(n/4);
n=n%4;
count=count+(n/3);
n=n%3;
count=count+(n/2);
n=n%2;
count=count+n;

printf("%d",count);


return 0;
}