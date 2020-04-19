#include<stdio.h>
#include<string.h>

int main()
{

    long long int t,n,i;
    scanf("%lld",&t);

    for(i=0;i<t;i++)
    {
        scanf("%lld",&n);
        if(n==1)
        {
            printf("1\n");
        }
        else if(n%2==0)
        {
            printf("%lld\n",(-n/2) );
        }
        else
        {
            printf("%lld\n",(-n/2)+1 );
        }
    }




}