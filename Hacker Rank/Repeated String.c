#include<bits/stdc++.h>
using namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,i,count=0,b,temp=0;
    scanf("%d",&n);
    int a[n];

    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }

    sort(a,a+n);

    for(i=0;i<n-1;i++)
    {
        if(a[i]==a[i+1])
        {
            b++;
        }
        else
        {
            b=1;
        }

        if(b>temp)
        {
            temp=b;
        }
    }

        printf("%d\n",n-temp );



}