#include<bits/stdc++.h>
using namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,a,i,j,temp,b=1;
    scanf("%d",&n);

    for(i=0;i<n;i++)
    {
        scanf("%d",&a);
        b=1;

        if(a>0)
        {
        for(j=1;j<=a;j++)
        {
            if(j%2==0)
            {
                b=b+1;
            }
            else
            {
                b=b*2;
            }
        }
        }
        printf("%d\n",b );
    }
            

}