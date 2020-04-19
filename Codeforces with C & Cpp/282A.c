#include<stdio.h>
#include <string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

int n,i,count=0;
scanf("%d",&n);
char str[n];
for(i=0;i<n;i++)
{
scanf("%s",str);

if((str[0]=='x' || str[0]=='X') && str[1]=='+' && str[2]=='+')
{
count++;
}

else if(str[0]=='+' && str[1]=='+' && (str[2]=='x' || str[2]=='X'))
{
count++;
}

else if((str[0]=='x' || str[0]=='X') && str[1]=='-' && str[2]=='-')
{
count=count-1;
}

else if(str[0]=='-' && str[1]=='-' && (str[2]=='x' || str[2]=='X'))
{
count--;
}


}

printf("%d",count);

}