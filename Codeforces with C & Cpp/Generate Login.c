#include<stdio.h>
#include<string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    char a[10],b[10];
    int i,l,c=0;
    scanf("%s%s",a,b);

    l=strlen(a);
    printf("%c",a[0] );

    for(i=1;i<l;i++)
    {
    	if(a[i]<b[0])
    	{
    		printf("%c",a[i] );
    	}
    	else
    	{
    		printf("%c\n",b[0] );
    		c=1;
    		break;
    	}
    }
    if(c!=1)
    {
    	printf("%c\n",b[0] );
    }


}