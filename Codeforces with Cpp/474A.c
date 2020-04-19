#include<stdio.h>
#include<string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    char a[31]="qwertyuiopasdfghjkl;zxcvbnm,./";
    char str[100],c;
    int len_a,len_b,i,j;

    scanf("%c%s",&c,str);

    len_a=strlen(a);
    len_b=strlen(str);



    if(c=='R')
    {
    	for(i=0;i<len_b;i++)

    	{
    		for(j=0;j<len_a;j++)
    		{
    			if(str[i]==a[j])
    			{
    				printf("%c",a[j-1] );
    				break;
    			}
    		}
    	}

    }
    else
    {
    	for(i=0;i<len_b;i++)

    	{
    		for(j=0;j<len_a;j++)
    		{
    			if(str[i]==a[j])
    			{
    				printf("%c",a[j+1] );
    				break;
    			}
    		}
    	}
    }



}