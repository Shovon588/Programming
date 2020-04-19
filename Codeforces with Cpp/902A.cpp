#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,m,i,x,count=1;
    scanf("%d%d",&n,&m);
    int a[n],b[m];

    for(i=0;i<n;i++)
    {
        scanf("%d%d",&a[i],&b[i]);
    }

    x=b[0];

    for(i=1;i<n;i++)
    {
        if(x>=a[i])
        {
            x=b[i];
            count++;
        }
        else
        {
            break;
        }
    }

    if(x>=m)
    {
        printf("YES");
    }
    else
    {
        printf("NO");
    }


    return 0;
}
