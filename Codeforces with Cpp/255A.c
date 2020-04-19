#include <bits/stdc++.h>
using  namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int a=1,b=2,c=3,n,i,x,chest=0,bicep=0,back=0;
    scanf("%d",&n);

    for(i=1;i<=n;i++)
    {
        scanf("%d",&x);

        if(i==a)
        {
            chest=chest+x;
            a=a+3;
        }
        else if(i==b)
        {
            bicep=bicep+x;
            b=b+3;
        }
        else if(i==c)
        {
            back=back+x;
            c=c+3;
        }
    }

    if(chest>=bicep && chest>=back)
    {
        printf("chest\n");
    }
    else if(bicep>=chest && bicep>=back)
    {
        printf("biceps\n");
    }
    else
    {
        printf("back\n");
    }

}

