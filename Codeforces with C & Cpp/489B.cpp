#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,m,i,j,count=0;
    scanf("%d",&n);
    int a[n];

    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    sort(a,a+n);
    scanf("%d",&m);
    int b[m];
    for(i=0;i<m;i++)
    {
        scanf("%d",&b[i]);
    }
    sort(b,b+m);

    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            if(a[i]==b[j] || a[i]==b[j]+1 || a[i]==b[j]-1)
            {
                count++;
                b[j]=-2;
                break;
            }
        }
    }
    printf("%d",count);

    return 0;
}
