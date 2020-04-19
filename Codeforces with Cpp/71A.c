#include<stdio.h>
#include <string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

int n,i,j,length;
char str[100];
scanf("%d",&n);


for(i=0;i<n;i++)
{
scanf("%s",str);
int count=0;
for(j=0;str[j]!='\0';j++)
{count++;}

if(count<=10)
{
printf("%s\n",str);
}
else{
printf("%c%d%c\n",str[0],count-2,str[count-1]);
}

}


}