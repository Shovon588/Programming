#include<bits/stdc++.h>
using namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif


    int i,pos=0;
    char str1[100],str2[100],len;
    scanf("%s",str1);
    scanf("%s",str2);
    
    len=strlen(str1);

    for(i=0;i<len;i++)
    {
    	if(str1[i]=='+')
    	{
    		pos++;
    	}
    	else
    	{
    		pos--;
    	}
    }



}