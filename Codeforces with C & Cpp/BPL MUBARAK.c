#include<stdio.h>
#include<string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int t,i,ball,l,j;
    scanf("%d",&t);
    char str[100];

    for(i=0;i<t;i++)
    {
    	scanf("%s",str);
    	l=strlen(str);

    	ball=0;

    	for(j=0;j<l;j++)
    	{
    		if(str[j]!='N' && str[j]!='W' && str[j]!='D')
    		{
    			ball++;
    		}
    	}
    	printf("%d\n",ball );
    }

}