#include<stdio.h>
int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif

    int n,m,a,b,temp,total=0;
    scanf("%d%d%d%d",&n,&m,&a,&b);

    if(b<(m*a))
    {
        total=(n/m)*b;
        n=n%m;
    }
    else
    {
        total=(n*a);
        n=0;
    }

    if(n*a>b)
    {
        total=total+b;
    }
    else
    {
        total=total+(n*a);
    }

    printf("%d\n",total );


}
