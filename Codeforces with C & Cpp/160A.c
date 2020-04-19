#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,i,half,temp,sum=0,j,count=0;
    scanf("%d",&n);
    int a[n];
    for(i=0;i<n;i++)
    {
    	scanf("%d",&a[i]);
    	sum=sum+a[i];
    }

    half=(sum/2)+1;

    for(i=0;i<n;i++)
    {
    	for(j=0;j<n;j++)
    	{
    		if(a[i]>a[j])
    		{
    		temp=a[i];
    		a[i]=a[j];
    		a[j]=temp;
    	}
    	}
    }
temp=0;
j=0;
while(temp<half)
{
	temp=temp+a[j];
	count++;
	j++;
}
printf("%d\n",count);
}