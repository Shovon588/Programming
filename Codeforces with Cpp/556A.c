#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

int n,i,one=0,zero=0,result;
scanf("%d",&n);
char str[n];
scanf("%s",str);

for(i=0;i<n;i++)
{
	if(str[i]=='1')
	{
		one++;
	}
	else
	{
		zero++;
	}
}

if(one<=zero)
{
	result=n-(2*one);
}
else
{
	result=n-(2*zero);
}

printf("%d\n",result );


}