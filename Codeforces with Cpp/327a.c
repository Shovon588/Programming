#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,i,one=0;
    scanf("%d",&n);
    int a[n];

    for(i=0;i<n;i++)
    {
    	scanf("%d",&a[i]);
    }

    for(i=0;i<n;i++)
    {

    	printf("%d--%d--%d\n",a[i-1],a[i],a[i+1] );

    	if(a[i]==1)
    	{
    		if(a[i-1]=='0' && a[i+1]=='0')
    		{
    			continue;
    		}
    		else
    		{
    			one++;
    			printf("%d--from me\n",one );
    		}
   		}
   		else
   		{
   			one++;
   			printf("%d--ami korechi\n",one );
   		}
    
    }

    printf("%d\n",one );


}


