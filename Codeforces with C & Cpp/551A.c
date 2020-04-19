#include<bits/stdc++.h>
using namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    
    int n,i,temp,j,k=0,temp1,count=0;
    scanf("%d",&n);
    int a[n],b[n];

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
    	for(j=0;j<n;j++)
    	{
    		if(a[i]==a[j])
    		{
    			count++;
    			a[j]=0;
    			a[i]=count;
    		}
    		else
    		{
    			count++;
    			a[i]=count;
    		}
    	}
    }

    for(i=0;i<n;i++)
    {
    	printf("%d\n",a[i] );
    }



}