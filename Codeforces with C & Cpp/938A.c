#include<bits/stdc++.h>
using namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif


    int n,i;
    char str[100];

    scanf("%d%s",&n,str);

    for(i=0;i<n;i++)
    {
    	if((str[i]=='a' || str[i]=='e' || str[i]=='i' || str[i]=='o' || str[i]=='u' || str[i]=='y') && (str[i+1]=='y' || str[i+1]=='a' || str[i+1]=='e' || str[i+1]=='i' || str[i+1]=='o' || str[i+1]=='u'))
    	{
    		continue;
    	}
    	else
    	{
    		printf("%c",str[i] );
    	}
    }


}