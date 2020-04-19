#include<bits/stdc++.h>
using namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,i,count,temp,j;
    scanf("%d",&n);
    int a[n];
    count=n;
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }


    sort(a,a+n);


count=n;
while(count>0)
{
    printf("%d\n",count );
    count=0;
    for(i=0;i<n;i++)
    {
        if(a[i]>0)
        {
            temp=a[i];
            break;
        }
    }

    for(i=0;i<n;i++)
    {
        if(a[i]>0)
        {
            a[i]=a[i]-temp;
        }
    }

    for(i=0;i<n;i++)
    {
        if(a[i]>0)
        {
            count++;
        }
    }
}
}