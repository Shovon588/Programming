#include<bits/stdc++.h>
using namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif


    char str[1000];
    int l,i,result=0,j,op,temp;

    scanf("%s",str);

    l=strlen(str);

    for(i=0;i<l;i++)
    {
    	if(str[i]=='+' || str[i]=='-')
    	{
    		break;
    	}
    	else
    	{
    		result=result+(str[i]-'0');
    	}
    }

    
    for(j=i;j<l-1;j++)
    {
    	if(str[j]=='+')
    	{
    		op=1;
    	}
    	else if(str[j]=='-')
    	{
    		op=-1;
    	}

    	temp=str[j+1]-'0';
    	j++;

    	result=result+(temp*op);
    }

    printf("%d\n",result );


}