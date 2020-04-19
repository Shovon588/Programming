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

    char str[n];

    scanf("%s",str);


    for(i=0;i<n;i++)
    {
    	if(str[i]=='1')
    	{
    		count++;
    	}
    }


    if(count>1)
    {
    	printf("1");

    	for(i=0;i<n-count;i++)
    	{
    		printf("0");
    	}
    }
    else
    {
    	printf("%s\n",str );
    }

    


}