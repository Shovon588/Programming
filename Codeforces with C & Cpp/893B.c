#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,i,j=0,temp,zero=0,one=0,real;
    scanf("%d",&n);
    int a[n/2];

    for(i=n/2;i>=1;i--)
    {
    	if(n%i==0)
    	{
    		a[j]=i;
    		j++;
    	}
    }

    for(i=0;i<j;i++)
    {
    	real=a[i];

    	while(a[i]>=1)
    	{
    		temp=a[i]%2;
    		if(temp==1)
    		{
    			one++;
    		}
    		else
    		{
    			zero++;
    		}
    		a[i]=a[i]/2;
    	}

    	if(one==zero+1)
    	{
    		printf("%d\n",real );
    		break;
    	}
    }


}