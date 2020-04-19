#include<bits/stdc++.h>
using namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif


    int n,m,i,j,count=0,b,k;
    scanf("%d%d",&n,&m);
    int a[n];

    for(i=0;i<n;i++)
    {
    	scanf("%d",&a[i]);
    }


    for(i=0;i<m;i++)
    {
    	scanf("%d",&b);

        for(j=b-1;j<n;j++)
        {
            for(k=b;k<n;k++)
            {
                if(a[j]==a[k])
                {
                    break;
                }
                else
                {
                    count++;
                    printf("%d--%d\n",count,k );
                }
            }
        }

    }



}