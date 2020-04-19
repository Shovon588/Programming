#include<stdio.h>
#include <string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

char str[100];
int i,count=1,a[100],j,temp,b;
scanf("%s",str);
for(i=0;str[i]!='\0';i++)
{
}
b=i;

for(i=1;i<b;i++)
{
if(str[i-1]==str[i])
{
count=count+1;
}
else
{
count=1;
}
a[i]=count;
}

for(i=0;i<b-1;i++)
{
for(j=i+1;j<b;j++)
{
if(a[j]>a[i])
{
temp=a[i];
a[i]=a[j];
a[j]=temp;
}
}
}

if(a[1]>=7)
{
printf("YES");
}
else
{
printf("NO");
}


}