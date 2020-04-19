#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif


int n,top,i,j,temp1,temp2,time=0;
scanf("%d%d",&n,&top);
int a[n],b[n],floor=top;

for(i=0;i<n;i++)
{
	scanf("%d%d",&a[i],&b[i]);
}

for(i=0;i<n;i++)
{
	for(j=0;j<n;j++)
	{
		if(a[i]>a[j])
		{
			temp1=a[i];
			a[i]=a[j];
			a[j]=temp1;
			temp2=b[i];
			b[i]=b[j];
			b[j]=temp2;
		}
	}
}

for(i=0;i<n;i++)
{
	time=time+floor-a[i];
	floor=a[i];

	if(time<b[i])
	{
		time=time+b[i]-time;
	}
}

printf("%d\n",time+floor );




}