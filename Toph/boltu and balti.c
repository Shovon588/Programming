#include<stdio.h>
int main()
{

    long long int a,b,i;
    char c;

    while(scanf("%lld", &a) != EOF)
    {
    
    	long long int sum=0;
    	scanf("%lld",&b);
    	for(i=a;i<=b;i++)
    	{
    		sum=sum+i;
    	}
    	printf("%lld\n",sum );

    }

}