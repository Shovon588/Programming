#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,i,j,temp,count=0,sum=0;
    scanf("%d",&n);
    int a[n];

    for(i=0;i<n;i++)
    {
    	scanf("%d",&a[i]);
    }

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

  	for(i=0;i<n;i++)
  	{
  	while(count+a[i]<=180)
  	{
  		count=count+a[i];
  		a[i]=0;
  		i++;
  	}
  	}

  	temp=0;
  	for(i=0;i<n;i++)
  	{
  		temp=temp+a[i];
  	}

  	if(temp>count)
  	{
  		printf("%d\n",temp-count );
  	}
  	else
  	{
  		printf("%d\n",count-temp );
  	}
}