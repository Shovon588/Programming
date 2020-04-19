#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,m,c=0,i,b,index,low,high,mid;
    scanf("%d",&n);
    int a[n];

    for (i=0;i<n;i++)
    {
        scanf("%d",&b);
        c=c+b;
        a[i]=c;
    }

    scanf("%d",&m);
    for(i=0;i<m;i++)
    {
        scanf("%d",&b);
        index=b;
        low=0,high=n-1,mid;

        for (int j=0;j<n;j++)
        {
            mid=(high+low)/2;

            if(high<low)
            {
                printf("%d\n",high+2);
                break;
            }

            if(a[mid]==index)
            {
                printf("%d\n",mid+1);
                break;
            }
            else if(a[mid]>index)
            {
                high=mid-1;
            }
            else
            {
                low=mid+1;
            }
        }
    }

    return 0;

}
