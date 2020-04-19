#include<stdio.h>
#include<string.h>

int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif

    long long int t,i,l,temp,n,a;
    char str[100005];
    scanf("%lld",&t);

    for(i=0;i<t;i++)
    {
        scanf("%s",str);
        l=strlen(str);

        n=1;
        temp=0;
        for(i=2;i<l;i++)
        {
            if(n!=i)
            {
                printf("%lld--hello--%lld\n",n,i);
            }

            a=n;
            n=temp+n;
            temp=a;
        }
    }

}