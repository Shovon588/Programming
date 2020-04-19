#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long int n,result;
    scanf("%lld",&n);

    n=n+1;

    if(n==1)
    {
        printf("0");
    }
    else if(n%2==0)
    {
        printf("%lld",n/2);
    }
    else
    {
        printf("%lld",n);
    }


    return 0;
}
