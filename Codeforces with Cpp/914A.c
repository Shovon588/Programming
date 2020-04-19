#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long int n,a,t,i;
    scanf("%lld",&t);

    for(i=0;i<t;i++)
    {
    scanf("%lld",&n);
    a=floor(sqrt(n));

    printf("%lld\n",(a+1)*(a+1) );
    }

}
