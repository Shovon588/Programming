#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

int n,i,temp,count=0,j,check;
scanf("%d",&n);
int a[n];

for(i=0;i<n;i++)
{
	scanf("%d",&a[i]);
}

for(i=0;i<n;i++)
{
	for(j=i+1;j<n;j++)
	{
		if(a[i]<=a[j])
		{
			temp=a[i];
			a[i]=a[j];
			a[j]=temp;
		}
	}
}

check=a[0];

for(i=1;i<n;i++)
{
	count=count+(check-a[i]);
}
printf("%d\n",count );


}