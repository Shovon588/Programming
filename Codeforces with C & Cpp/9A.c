#include <bits/stdc++.h>
using  namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int x,y,big;
    scanf("%d%d",&x,&y);

    if(x>y)
    {
        big=x;
    }
    else
    {
        big=y;
    }

    big=6-big+1;

    if(big==6)
    {
        printf("1/1\n");
    }
    else if(big==4)
    {
        printf("2/3\n");
    }
    else if(big==3)
    {
        printf("1/2\n");
    }
    else if(big==2)
    {
        printf("1/3\n");
    }
    else
    {
        printf("%d/6\n",big);
    }

}

