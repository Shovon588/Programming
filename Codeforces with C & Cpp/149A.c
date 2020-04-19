#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

int n,i,j,temp,a[12],count=0,month=0;
scanf("%d",&n);

for(i=0;i<12;i++)
{
	scanf("%d",&a[i]);
}

for(i=0;i<12;i++)
{
	for(j=i+1;j<12;j++)
	{
		if(a[i]<a[j])
		{
			temp=a[i];
			a[i]=a[j];
			a[j]=temp;
		}
	}
}

for(i=0;i<12;i++)
{
	month=month+a[i];
	if(n==0)
	{
		printf("0\n");
		break;
	}
	else if(month>=n)
	{
		printf("%d\n",count+1 );
		break;
	}
	else
	{
		count++;
	}
}

if(month<n)
{
	printf("-1\n");
}



}