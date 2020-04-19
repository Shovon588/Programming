#include<stdio.h>
int main()
{

    int t,i,j;
    long long int n,a,b,m,sum=0;
    scanf("%d",&t);

    for(i=0;i<t;i++)
    {
    	scanf("%lld%lld%lld%lld",&n,&a,&b,&m);
    	sum=0;

    	for(j=1;j<=n;j++)
    	{
    		if(j%a==0 || j%b==0)
    		{
    			sum=sum+j;
    		}
    	}

    	printf("%lld\n",sum%m );
    }

}