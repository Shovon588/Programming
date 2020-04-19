#include<bits/stdc++.h>
using namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif


    long long int n,a,t,i;
    scanf("%lld",&t);

    for(i=0;i<t;i++)
    {
    scanf("%lld",&n);
    a=floor(sqrt(n));

    printf("%lld\n",(a+1)*(a+1) );
    }

}