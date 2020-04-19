#include<stdio.h>
#include<string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    long long int n,l,i,j,temp;
    scanf("%lld%lld",&n,&l);
    long long int a[n],b[n+1];

    for(i=0;i<n;i++)
    {
    	scanf("%lld",&a[i]);
    }


    for(i=0;i<n;i++)
    {
    	for(j=0;j<n;j++)
    	{
    		if(a[i]<a[j])
    		{
    			temp=a[i];
    			a[i]=a[j];
    			a[j]=temp;
    		}
    	}
    }

    if(a[0]!=0)
    {
    	b[0]=2*a[0];
	}
	else
	{
		b[0]=0;
	}


    for(i=1;i<n;i++)
    {
    	b[i]=a[i]-a[i-1];
    }

    b[n]=2*(l-a[n-1]);

    for(i=0;i<n+1;i++)
    {
    	for(j=0;j<n+1;j++)
    	{
    		if(b[i]>b[j])
    		{
    			temp=b[i];
    			b[i]=b[j];
    			b[j]=temp;
    		}
    	}
    }

    printf("%f\n",b[0]/2.0 );

}