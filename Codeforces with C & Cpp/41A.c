#include<stdio.h>
#include<string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

char str1[200],str2[200];
int i,a,j=0,count=0;
scanf("%s%s",str1,str2);
a=strlen(str1);

for(i=a-1;i>=0;i--)
{
if(str1[i]==str2[j])
{
count++;
}

j=j+1;
}

if(count==a)
{
printf("YES");
}
else
{
printf("NO");
}
return 0;
}