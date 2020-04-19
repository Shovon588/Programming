#include<bits/stdc++.h>
using namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,i,count=0;
    scanf("%d",&n);
    int a[n];

    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }

    for(i=1;i<n;i++)
    {
        if(a[i]==0 && a[i+1]==1)
        {
            count=count+1;
            i=i+1;
        }
        else if(a[i]==0 && a[i+1]==0)
        {
            count++;
        }
    }
printf("%d\n",count );
    

}