#include<bits/stdc++.h>
using namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif


    char str[5005];
    int l,i,a=0,b=0,c=0,check=0;

    scanf("%s",str);

    l=strlen(str);

    for(i=0;i<l;i++)
    {
    	if(check==0 && str[i]=='a')
    	{
    		a++;
    	}
    	else if(check==0 && str[i]!='a')
    	{
    		check++;
    		i--;
    	}
    	else if(check==1 && str[i]=='b')
    	{
    		b++;
    	}
    	else if(check==1 && str[i]!='b')
    	{
    		check++;
    		i--;
    	}
    	else if(check==2 && str[i]=='c')
    	{
    		c++;
    	}
    	else if(check==2 && str[i]!='c')
    	{
    		check++;
    		i--;
    	}
    	else
    	{
    		break;
    	}
    }


    if(a==0 || b==0 || c==0)
    {
    	printf("NO\n");
    }
    else if(a==c || b==c || (a+b)==c)
    {
    	printf("YES\n");
    }


    


}