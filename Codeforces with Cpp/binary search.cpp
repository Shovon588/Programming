#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,i,first,last,mid,b;
    scanf("%d",&n);
    int a[n];


    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }

    scanf("%d",&b);

    first=0;
    last=n-1;

    while(first<=last)
    {
        mid=(first+last)/2;

        if(a[mid]==b)
        {
            printf("%d",mid);
            break;
        }
        else if(a[mid]<b)
        {
            first=mid+1;
        }
        else if(a[mid]>b)
        {
            last=mid-1;
        }
    }




 return 0;

}
