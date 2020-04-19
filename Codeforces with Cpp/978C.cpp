#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long int n,m,i,j,b,temp=0,flag=0;
    scanf("%lld%lld",&n,&m);
    long long int a[n];

    for(i=0;i<n;i++)
    {
        scanf("%lld",&b);
        temp=temp+b;
        a[i]=temp;
    }

    temp=0;
    for(i=0;i<m;i++)
    {
        scanf("%lld",&b);

        for(j=flag;j<n;j++)
        {
            if(b>=temp && b<=a[j])
            {
                printf("%lld %lld\n",j+1,b-temp);
                flag=j;
                break;
            }
            else
            {
                temp=a[j];
            }
        }
    }

 return 0;
}
