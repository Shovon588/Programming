#include<stdio.h>
#include <string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

char str[100];
int i,temp,j,count=0,distinct;
scanf("%s",str);
for(i=0;str[i]!='\0';i++)
{
temp=i+1;
}

for(i=0;i<temp-1;i++)
{
for(j=i+1;j<temp;j++)
{
if(str[i]==str[j])
{
count++;
break;
}
}
}

distinct=temp-count;


if(distinct%2==0)
{
printf("CHAT WITH HER!");
}
else{
printf("IGNORE HIM!");
}



}