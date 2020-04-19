#include<bits/stdc++.h>
using namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    
    long long int p,y;


    scanf("%lld%lld",&p,&y);

    if(y%2==0)
    {
    	y=y-1;	
    }


    if(y>p)
    {
    	printf("%lld\n",y );
    }
    else
    {
    	printf("-1\n");
    }





}