#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

int n,p,i,temp,j,c=0,low=10000;
scanf("%d%d",&n,&p);
int a[p],b[10];

for(i=0;i<p;i++)
{
	scanf("%d",&a[i]);
}

for(i=0;i<p;i++)
{
	for(j=0;j<p;j++)
	{
		if(a[i]<a[j])
		{
			temp=a[i];
			a[i]=a[j];
			a[j]=temp;
		}
	}
}

	for(i=0;i<p-n+1;i++)
	{
		b[c]=a[n-1+i]-a[i];

		if(b[c]<low)
		{
			low=b[c];
		}
		c++;

	}
	printf("%d\n",low );


}