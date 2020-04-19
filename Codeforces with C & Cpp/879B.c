#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

int n,k,i,p1,p2,count;
scanf("%d%d",&n,&k);
int a[n];

for(i=0;i<n;i++)
{
	scanf("%d",&a[i]);
}

p1=a[0];
p2=a[1];

for(i=2;i<n;i++)
{
if(p1>p2)
	{
		count++;

		printf("%d--%d--%d\n",p1,p2,count );
		if(count==k)
		{
			printf("%d\n",p1 );
			break;
		}
		p2=a[i];
	}
	else
	{
		p1=p2;
		p2=a[i];
		count=0;
	}
}


}