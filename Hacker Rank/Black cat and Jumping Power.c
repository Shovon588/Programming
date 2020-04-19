#include<bits/stdc++.h>
using namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    long long int n,a,b,i;
    float x,y;
    scanf("%lld",&n);

    for(i=0;i<n;i++)
    {
        scanf("%lld%lld",&a,&b);

        x=sqrt(a);
        y=sqrt(b);


        printf("%.0f\n",floor(y)-ceil(x)+1 );
    }
}