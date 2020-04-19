#include<bits/stdc++.h>
using namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif


    int n,i,count=0;

    char str[100];
    scanf("%d%s",&n,str);

    for(i=0;i<n;i++)
    {
    	if((str[i]=='U' && str[i+1]=='R') || (str[i]=='R' && str[i+1]=='U'))
    	{
    		count++;
    		i++;
    	}
    }

    printf("%d\n", n-count);



}


