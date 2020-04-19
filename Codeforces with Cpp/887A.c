#include<stdio.h>
#include<string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

char str[100];
int i,n,j,count=0;
scanf("%s",str);

n=strlen(str);

for(i=0;i<n;i++)
{
	if(str[i]=='1')
	{
		break;
	}
}

for(j=i+1;j<n;j++)
{
	if(str[j]=='0')
	{
		count++;
	}
}
if(count>=6)
{
	printf("yes\n");
}
else
{
	printf("no\n");
}

}