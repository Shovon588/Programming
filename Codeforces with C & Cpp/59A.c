#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

char str[200];
int i,high=0,low=0;
scanf("%s",str);
for(i=0;str[i]!='\0';i++)
{
if(str[i]>=65 && str[i]<=90)
{
high++;
}
else
{low++;}
}
if(high>low)
{
for(i=0;str[i]!='\0';i++)
{
if(str[i]>=97 && str[i]<=122)
{
str[i]=str[i]-32;
}
}
}
else if(high<=low)
{
for(i=0;str[i]!='\0';i++)
{
if(str[i]>=65 && str[i]<=90)
{
str[i]=str[i]+32;
}
}
}
printf("%s",str);

return 0;
}