#include<stdio.h>
#include <string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

char str[100];
int i,count=0;
scanf("%s",str);
for(i=0;str[i]!='\0';i++)
{
if(str[i]=='h')
{
count=count+1;
break;
}
}
for(i=i+1;str[i]!='\0';i++)
{
if(str[i]=='e')
{
count=count+1;
break;
}
}
for(i=i+1;str[i]!='\0';i++)
{
if(str[i]=='l')
{
count=count+1;
break;
}
}
for(i=i+1;str[i]!='\0';i++)
{
if(str[i]=='l')
{
count=count+1;
break;
}
}
for(i=i+1;str[i]!='\0';i++)
{
if(str[i]=='o')
{
count=count+1;
break;
}
}

if(count==5)
{
printf("YES");
}
else

{
printf("NO");
}


}