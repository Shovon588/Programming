#include<stdio.h>
#include<string.h>
int main()
{

    char str[100];
    int i,a;
    scanf("%[^\n]s",str);
    a=strlen(str);

    for(i=0;i!=a;i++)
    {
    	if(str[i]==32)
    	{
    		continue;
    	}
    	else
    	{
    		printf("%c",str[i] );
    	}
    }


    return 0;
}