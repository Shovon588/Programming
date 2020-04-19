#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif


int n,i,a[20],j,k=0,count=0,temp,case1,case2;
scanf("%d",&n);
for(i=0;i<n;i++)
{
	for(j=0;j<6;j++)
	{
		scanf("%d",&a[k]);
		if(a[k]==0)
		{
			count++;
		}
		k++;
	}
}

for(i=0;i<k;i++)
{
	if(a[i]==0)
	{
		i++;
	}

	for(j=i+1;j<k;j++)
	{
		if(a[i]>=a[j])
			{
				temp=a[i];
				a[i]=a[j];
				a[j]=temp;
			}
	}
}

for (i=0;i<k;i++)
{
	printf("%d--%d\n",a[i],i );
}

for(i=count;i<k;i++)
{
	if(a[i]==a[i+1])
	{
		if(a[i+2]=a[i+1]+1)
		{
			i=i+1;
		}
}
else
	{
		printf("im breaking at %d\n",i );
		printf("%d\n",a[i] );
		break;
	}
}

case1=(a[i]*10)+a[i-1];
case2=(a[i-1]*10)+a[i-2];
printf("%d--%d--%d\n",case2,case1,a[i-1] );

if(count>0)
{
	if(a[i]==a[i-1]+1)
	{
		printf("%d\n",case1 );
	}
	else if(a[i]!=a[i-1]+1)
	{
		printf("%d\n",case2);
	}
}


}