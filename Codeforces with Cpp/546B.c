#include <bits/stdc++.h>
using  namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif


    int n,i,x,count=0,j;
    scanf("%d",&n);

    int a[3005]={0};

    for(i=0;i<n;i++)
    {
        scanf("%d",&x);

        if(a[x]==0)
        {
            a[x]++;
        }
        else
        {
            for(j=x+1;j<3005;j++)
            {
                count++;
                if(a[j]==0)
                {
                    a[j]++;
                    break;
                }
                
            }
        }
    }
    printf("%d\n",count );

}

