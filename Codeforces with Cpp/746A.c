#include <bits/stdc++.h>
using  namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int a,b,c,d=0;
    scanf("%d%d%d",&a,&b,&c);

    while(a>0)
    {
        if(b>=2*a && c>=4*a)
        {
            printf("%d\n",a+2*a+4*a );
            d=1;
            break;
        }
        a--;
    }
    if(d==0)
    {
        printf("0\n");
    }

}

