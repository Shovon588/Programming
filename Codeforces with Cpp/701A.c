#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

int n,i,sum=0,temp,j;
scanf("%d",&n);
int a[n];

for(i=0;i<n;i++)
{
	scanf("%d",&a[i]);
	sum=sum+a[i];
}

temp=sum/(n/2);

for(i=0;i<n;i++)
{

	for(j=0;j<n;j++)
	{
		if(i!=j)
		{
			if(a[i]+a[j]==temp)
			{
				printf("%d %d\n",i+1,j+1 );
				a[i]=0;
				a[j]=0;
			}
		}
	}
}


}