#include<stdio.h>
#include<string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,i,j,count=1,total=1;
    scanf("%d",&n);
    int a[n],b[n],tempa,tempb;

    scanf("%d%d",&a[0],&b[0]);
    tempa=a[0];
    tempb=b[0];


    for(i=1;i<n;i++)
    {
    	scanf("%d%d",&a[i],&b[i]);

    	if(a[i]==tempa && b[i]==tempb)
    	{
    		count++;
    		if(count>total)
    		{
    			total=count;
    		}
    	}
    	else
    	{
    		tempa=a[i];
    		tempb=b[i];
    		count=1;
    	}

    }


    printf("%d\n",total );
}