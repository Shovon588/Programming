#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,i;
    long long int a,b,temp;
    scanf("%d",&n);
  	
  
    for(i=0;i<n;i++)
    {
    	scanf("%lld%lld",&a,&b);

    	if(a%b==0)
    	{
    		temp=a;
    	}
    	else if(b%a==0)
    	{
    		temp=b;
    	}
    	else
    	{
    		temp=a*b;
    	}


    	if(temp==(a*b))
    	{
    		printf("yes\n");
    	}
    	else
    	{
    		printf("no\n");
    	}
    }


}