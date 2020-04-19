#include<stdio.h>
#include <string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

char str[1000];
int i,count=0,j;
scanf("%s",str);


if(str[0]>=97 && str[0]<=122)
{
str[0]=str[0]-32;
printf("%c",str[0]);
for(i=1;str[i]!='\0';i++)
{
printf("%c",str[i]);
}
}
else
{
printf("%s",str);
}



}