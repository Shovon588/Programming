#include<stdio.h>
#include<string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,i,a,left=0,right=0,up=0,down=0,result;
    scanf("%d",&n);
    char str[n];
    scanf("%s",str);
    a=strlen(str);

    for(i=0;i<a;i++)
    {
    	if(str[i]=='L')
    	{
    		left++;
    	}
    	else if(str[i]=='R')
    	{
    		right++;
    	}
    	else if(str[i]=='U')
    	{
    	    up++;
    	}
    	else if(str[i]=='D')
    	{
    		down++;
    	}

    }

if(left<right)
{
	result=result+(left*2);
}
else
{
	result=result+(right*2);
}

if(up<down)
{
	result=result+(up*2);
}

else
{
	result=result+(down*2);
}

printf("%d\n",result );

}