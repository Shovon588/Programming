#include<stdio.h>
#include <string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

int i;
char str[99];
scanf("%s",str);
for(i=0;str[i]!='\0';i++)
{
if(str[i]!='a' && str[i]!='A' && str[i]!='e' && str[i]!='E' && str[i]!='i' && str[i]!='I' && str[i]!='o' && str[i]!='O' && str[i]!='u' && str[i]!='U' && str[i]!='y' && str[i]!='Y')
{
if(str[i]>=65 && str[i]<=90)
{
printf(".%c",str[i]+32);
}
else{printf(".%c",str[i]);}
}
}


}