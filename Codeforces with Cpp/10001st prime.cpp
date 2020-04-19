#include<bits/stdc++.h>
using namespace std;
int main()
{
    int a[10001],i;

    a[0]=a[1]=0;
    for(i=2;i<=10001;i++)
    {
        a[i]=i;
    }

    for(i=2;i<=10001;i++)
    {
        for(int j=i+1;j<=10001;j++)
        {
            if(a[j]%i==0)
            {
                a[j]=0;
            }
        }
    }

    for(i=2;i<=100;i++)
    {
        printf("%d",a[i]);
    }


 return 0;
}
