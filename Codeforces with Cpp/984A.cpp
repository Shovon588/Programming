#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,i,j,k;
    scanf("%d",&n);
    int a[n];

    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }

    sort(a,a+n);



    i=1;
    j=n-1;
    k=0;
    while(i<n)
    {
        if(i%2!=0)
        {
            a[j]=0;
            j--;
        }
        else
        {
            a[k]=0;
            k++;
        }
        i++;
    }

    sort(a,a+n);

    printf("%d",a[n-1]);



    return 0;
}
