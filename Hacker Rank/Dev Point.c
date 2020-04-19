#include<bits/stdc++.h>
using namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif


    long long int n,m,q,i,x,y,l,r,j,k,t,z;
    scanf("%lld",&t);

    for(z=0;z<t;z++)
    {

    scanf("%lld%lld%lld",&n,&m,&q);
    long long int a[n],b[m];


    for(i=1;i<=n;i++)
    {
        scanf("%lld",&a[i]);
    }

    for(i=1;i<=m;i++)
    {
        scanf("%lld",&b[i]);
    }

    for(i=0;i<q;i++)
    {
        scanf("%lld%lld%lld%lld",&x,&y,&l,&r);

        for(j=l;j<=r;j++)
        {
            for(k=x;k<=y;k++)
            {
                a[j]=a[j]+b[k];
            }
        }
    }

    printf("Case %lld:\n%lld",z+1,a[1] );
    for(i=2;i<=n;i++)
    {
        printf(" %lld",a[i] );
    }
    printf("\n");
}

}