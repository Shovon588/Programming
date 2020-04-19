#include<stdio.h>
#include <string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

long long int n,m,a,d,i,temp=0,count=0,j,emp;
scanf("%lld%lld%lld%lld",&n,&m,&a,&d);
long long int b[m];

for(i=0;i<m;i++)
{
	scanf("%lld",&b[i]);
}

for(i=0,j=1;i<m,j<=n;i++,j++)
{
	emp=j*a;
	printf("%lld\t%lld\n",temp,emp );
	if((b[i]-temp<=d) || (emp-temp<=d))
	{
		if(b[i]>=emp)
		{
			temp=b[i];
		}
		else
		{
			temp=emp;
		}
			
		continue;
	}
	else
	{
		count++;
		if(b[i]>=emp)
		{
			temp=b[i];
		}
		else
		{
			temp=emp;
		}
		printf("%lld\t%lld\n",temp,emp );
	}
}
printf("%lld\n",count );

}