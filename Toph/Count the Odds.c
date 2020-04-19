#include<stdio.h>
#include<string.h>

int main()
{


    long long int a,b;

        scanf("%lld%lld",&a,&b);

        if(a%2!=0 && b%2!=0)
        {
            printf("%lld\n",((b-a)/2)+1 );
        }
        else if((a%2==0 && b%2!=0) || (a%2!=0 && b%2==0))
        {
            printf("%lld\n",((b-a)/2)+1 );
        }
        else
        {
            printf("%lld\n",(b-a)/2 );
        }

}