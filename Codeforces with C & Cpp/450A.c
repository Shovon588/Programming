#include <bits/stdc++.h>
using  namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif


    int i,j,n,m,max=-1,rem,num;
    scanf("%d%d",&n,&m);
    for(i=0;i<n;i++)
    {
        scanf("%d",&num);
        j=(num/m);
        if((num%m)>0)
        {
            j++;
        }
        if(max<=j)
        {
            max=j;
            rem=i+1;
        }
    }
    printf("%d\n",rem);
}

