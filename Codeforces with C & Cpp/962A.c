#include<bits/stdc++.h>
using namespace std;
int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif


    int n,i,total=0;
    float half;

    scanf("%d",&n);
    int a[n];

    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);

        total=total+a[i];
    }
    
    half=float(total)/2.0;
    half=ceil(half);

    total=0;
    for(i=0;i<n;i++)
    {
        total=total+a[i];

        if(total>=half)
        {
            break;
        }
    }

    printf("%d\n",i+1 );

    return 0;
}
