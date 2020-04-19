#include<bits/stdc++.h>
using namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    long long int n;
    scanf("%lld",&n);


    if(n==1 || n%114==0 || n%144==0)
    {
    	printf("YES\n");
    }
    else
    {
    	printf("NO\n");
    }


}