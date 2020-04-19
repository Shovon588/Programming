#include<stdio.h>
#include <string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

char str[100];
int i,count=0,j;
scanf("%s",str);

for(i=0;str[i]!='\0';i++)
{
if(str[i]>=65 && str[i]<=90)
{
count++;
}
}

if(count==i)
{
for(j=0;j<i;j++)
{
str[j]=str[j]+32;
printf("%c",str[j]);
}
}
else if(count==i-1 && (str[0]>=97 && str[0]<=122))
{
str[0]=str[0]-32;
printf("%c",str[0]);
for(j=1;j<i;j++)
{
str[j]=str[j]+32;
printf("%c",str[j]);
}
}
else
{
printf("%s",str);
}

return 0;

}