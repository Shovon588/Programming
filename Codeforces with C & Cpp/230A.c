#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,s,i,count=0,tempa,tempb,j;
    scanf("%d%d",&s,&n);
    int a[n],b[n];

    for(i=0;i<n;i++)
    {
    	scanf("%d%d",&a[i],&b[i]);
    }

    for(i=0;i<n;i++)
    {
    	for(j=0;j<n;j++)
    	{
    		if(a[i]<a[j])
    		{
    			tempa=a[i];
    			tempb=b[i];
    			a[i]=a[j];
    			b[i]=b[j];
    			a[j]=tempa;
    			b[j]=tempb;
    		}
    	}
    }

    for(i=0;i<n;i++)
    {
    	if(s>a[i])
    	{
    		s=s+b[i];
    		count++;
    	}
    	else
    	{
    		break;
    	}
    }

    if(count==n)
    {
    	printf("YES\n");
    }
    else
    {
    	printf("NO\n");
    }

}