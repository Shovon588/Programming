#include<bits/stdc++.h>
using namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif


    int a,b,i,gcd;

    scanf("%d%d",&a,&b);


    for(i=0;i<=a && i<=b;i++)
    {
    	if(a%i==0 && b%i==0)
    	{
    		gcd=i;
    		break;
    	}
    }

    printf("%d\n",gcd );
    


}