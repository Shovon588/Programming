#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif


    long long int a,b;
    scanf("%lld%lld",&a,&b);


    if(a>=(2*b))
    {
        a=a%b;
    }


    if(b>=(2*a))
    {
        b=b%a;
    }

    if(a>=(2*b))
    {
        a=a-(2*b);
    }
    else if(b>=(2*a))
    {
        b=b-(2*a);
    }



    printf("%lld %lld\n",a,b );
    


}