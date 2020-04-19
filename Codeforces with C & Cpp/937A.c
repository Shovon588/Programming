#include<bits/stdc++.h>
using namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    
    int n,i,count=1,j=0,a,b[105],k;
    scanf("%d",&n);

    for(i=0;i<n;i++)
    {
    	scanf("%d",&a);

    	if(a!=0)
    	{
    		b[j]=a;
    		j++;
    	}
    }

    if(j==0)
    {
    	count=0;
    }


    sort(b,b+j);


    for(i=0;i<j-1;i++)
    {
    	if(b[i]==b[i+1])
    	{
    		continue;
    	}
    	else
    	{
    		count++;
    	}
    }
printf("%d\n",count );


}