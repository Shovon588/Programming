#include<bits/stdc++.h>
using namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,i,count=1,w;
    scanf("%d",&n);
    int a[n];

    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }

    sort(a,a+n);

    w=a[0];

    for(i=1;i<n;i++)
    {
        if(a[i]>=w &&  a[i]<=(w+4))
        {
            continue;
        }
        else
        {
            count++;
            w=a[i];
        }
    }
    printf("%d\n",count );


}