#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,t,i;
    scanf("%d",&t);
    int a[1005];
    float check;

    for(i=0;i<t;i++)
    {
        scanf("%d",&a[i]);
    }
    sort(a,a+t);

    for(i=t-1;i>=0;i--)
    {
        check=sqrt(a[i]);
        if(check!=floor(check))
        {
            printf("%d",a[i]);
            break;
        }

    }

}
