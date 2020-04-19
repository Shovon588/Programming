#include<stdio.h>
#include <string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

char str[100];
int count=0,i;
scanf("%s",str);
for(i=0;str[i]!='\0';i++)
{
if(str[i]=='H' || str[i]=='Q' || str[i]=='9')
{
count++;
}
}
if(count>0)
{
printf("YES");
}
else
{
printf("NO");
}
}