#include <bits/stdc++.h>
using  namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif


    int n,i,b,a,temp=0;
    scanf("%d",&n);
    char str[100];

    for(i=0;i<n;i++)
    {
        scanf("%s %d%d",str,&b,&a);

        if(b>=2400 && a>b)
        {
            temp=1;
        }
    }

    if(temp==0)
    {
        printf("NO\n");
    }
    else
    {
        printf("YES\n");
    }

}

