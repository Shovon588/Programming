#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif


int n,i,count=0,j;
scanf("%d",&n);
long long int a[n];

for(i=0;i<n;i++)
{
	scanf("%lld",&a[i]);
}

for(i=0;i<n;i++)
{
	count=0;

	if(a[i]%2==0)
	{

	for(j=2;j<a[i]-1;j++)
	{
		if(a[i]%j==0)
		{
			count++;
			if(count>1)
			{
				break;
			}
		}
	}
}
	else 
	{

	for(j=3;j<a[i]-1;j=j+2)
	{
		if(a[i]%j==0)
		{
			count++;
			if(count>1)
			{
				break;
			}
		}
	}
	}

		
		if(count>1 || count<1 || count==0)
		{
			printf("NO\n");
		}
		else
		{
			printf("YES\n");
		}		


}

}