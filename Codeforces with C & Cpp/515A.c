#include<stdio.h>
#include<string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    long long int a,b,c,sum;
    scanf("%lld%lld%lld",&a,&b,&c);
    if(a<0)
    {
    	a=(a*-1);
    }

    if(b<0)
    {
    	b=(b*-1);
    }
    
    sum=a+b;



    if(sum==c)
    {
    	printf("Yes\n");
    }
    else if(sum<c && c%2==0 && sum%2==0)
    {
    	printf("Yes\n");
    }
    else if(sum<c && c%2!=0 && sum%2!=0)
    {
    	printf("Yes\n");
    }
    else
    {
    	printf("No\n");
    }

}