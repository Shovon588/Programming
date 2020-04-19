#include<bits/stdc++.h>
using namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,k,i,tempa,tempb,count=0,j;
    scanf("%d%d",&n,&k);
    int a[n],b[n],c[105];

    for(i=0;i<n;i++)
    {
    	scanf("%d",&a[i]);
    	b[i]=i+1;
    }

    for(i=0;i<n;i++)
    {
    	for(j=0;j<n;j++)
    	{
    		tempa=a[i];
    		tempb=b[i];
    		a[i]=a[j];
    		b[i]=b[j];
    		a[j]=tempa;
    		b[j]=tempb;
    	}
    }

    j=0;
    tempa=0;
    for(i=0;i<n;i++)
    {
    	if(count+a[i]<=k)
    	{
    		count=count+a[i];
    		c[j]=b[i];
    		j++;
    		tempa++;
    	}
    	else
    	{
    		break;
    	}
    }

    printf("%d\n",tempa );
    if(tempa!=0)
    {
    printf("%d",c[0] );
    for(i=1;i<j;i++)
    {
    	printf(" %d",c[i] );
    }
	}


}