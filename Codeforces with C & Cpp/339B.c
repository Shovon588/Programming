#include<stdio.h>
#include <string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

int n,i,count=0;
scanf("%d",&n);
char str[n],temp;
scanf("%s",str);
temp=str[0];
for(i=1;i<n;i++)
{
if(temp==str[i])
{
count++;
}
else
{
temp=str[i];
}
}

printf("%d",count);

}