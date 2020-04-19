#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,i;
    scanf("%d",&n);
    int a[n],j,b[50];

    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }

    for(i=n-1;i>=0;i--)
    {
        for(j=i-1;j>=0;j--)
        {
            if(a[i]==a[j])
            {
                a[j]=0;
            }
        }
    }

    j=0;
    for(i=0;i<n;i++)
    {
        if(a[i]!=0)
        {
            b[j]=a[i];
            j++;
        }
    }
    printf("%d\n",j);
    printf("%d",b[0]);

    for(i=1;i<j;i++)
    {
        printf(" %d",b[i]);
    }

    return 0;
}
