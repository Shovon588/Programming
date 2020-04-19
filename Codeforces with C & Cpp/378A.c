#include <bits/stdc++.h>
using  namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int a,b,temp,win=0,loss=0,draw=0,c,d,i;
    scanf("%d%d",&a,&b);

    for(i=1;i<=6;i++)
    {
        c=a-i;
        d=b-i;

        if(c<0)
        {
            c=c*-1;
        }
        if(d<0)
        {
            d=d*-1;
        }

        if(c==d)
        {
            draw++;
        }
        else if(c<d)
        {
            win++;
        }
        else
        {
            loss++;
        }
    }
    printf("%d %d %d\n",win,draw,loss );

}

