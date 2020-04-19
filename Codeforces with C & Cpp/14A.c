#include <bits/stdc++.h>
using  namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif


    int n,m,i,j;
    char c,a;
    scanf("%d%d",&n,&m);

    scanf("%c",&a);

    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            scanf("%c%c",&c,&a);
        }
        scanf("%c",&a);
    }


    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            printf("%c",c );
        }
        printf("\n");
    }


}

