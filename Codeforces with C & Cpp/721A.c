#include<stdio.h>
#include<string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

int n,i,count=0,a,j,b[100];
scanf("%d",&n);
char str[n];
scanf("%s",str);
a=strlen(str);

j=0;
for(i=0;i<a;i++)
{
	if(str[i]=='B')
	{
		while(i<a && str[i]!='W')
		{
			count++;
			i++;
		}
	}
	if(count>0)
	{
		b[j]=count;
		j++;
	}
	count=0;
}

if(j!=0)
{
printf("%d\n%d",j,b[0] );
for(i=1;i<j;i++)
{
	printf(" %d",b[i] );
}
}
else
{
	printf("0\n");
}

}