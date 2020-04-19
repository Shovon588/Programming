#include<bits/stdc++.h>
using namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int t,n,k,i,count,a,j;
    scanf("%d",&t);

    for(i=0;i<t;i++)
    {
        count=0;
        scanf("%d%d",&n,&k);

        for(j=0;j<n;j++)
        {
            scanf("%d",&a);
            if(a<=0)
            {
                count++;
            }
        }
        
        if(count>=k)
        {
            printf("NO\n");
        }
        else
        {
            printf("YES\n");
        }
    }
            

}