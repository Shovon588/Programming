#include<stdio.h>
#include<string.h>
int main()
{


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

    	if(ball<6)
    	{
    		printf("%d BALLS\n",ball );
    	}
    	else if(ball==6)
    	{
    		printf("6 BALLS\n1 OVER\n" );
    	}
    	else
    	{
    		printf("%d BALLS\n%d OVER %d BALLS\n",ball,ball/6,ball%6 );
    	}
    }

}