#include<bits/stdc++.h>
using namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif


    int n,m,i,count=1,one=1,big=1005;
    scanf("%d%d",&n,&m);
    int a[m];

    for(i=0;i<m;i++)
    {
    	scanf("%d",&a[i]);
    }

    sort(a,a+m);

        for(i=0;i<m-1;i++)
    {
        if(a[i]==a[i+1])
        {
            one++;
            continue;
        }
        else
        {
            if(one<big)
            {
                big=one;
            }
            one=1;
            count++;
        }
    }

    if(one<big)
    {
    	big=one;
    }

    if(count==n)
    {
    	printf("%d\n",big );
    }
    else
    {
    	printf("0\n");
    }
}


