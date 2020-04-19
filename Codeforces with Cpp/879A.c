#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

int n,i,j,day;
scanf("%d",&n);
int s[n],d[n],temp;

for(i=0;i<n;i++)
{
	scanf("%d%d",&s[i],&d[i]);
}

day=s[0];

for(i=1;i<n;i++)
{
	j=1;
	temp=s[i];
	while(s[i]<=day)
	{
		s[i]=temp+(j*d[i]);
		j++;
	}
	day=s[i];
}

printf("%d\n",day );

}