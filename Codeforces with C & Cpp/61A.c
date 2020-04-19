#include<stdio.h>
#include <string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif


char str1[200],str2[200];
int i,j;
scanf("%s%s",str1,str2);
for(i=0;str1[i]!='\0';i++)
{
if(str1[i]!=str2[i])
{
printf("1");
}
else
{
printf("0");
}
}


return 0;
}