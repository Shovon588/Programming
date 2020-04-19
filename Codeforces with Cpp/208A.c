#include<stdio.h>
#include<string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    char str[200];
    int a,i,j,temp=0,temp1=0;

    scanf("%s",str);
    a=strlen(str);


    for(i=0;i<a;i++)
    {
    	if(str[i]!='W' || str[i+1]!='U' || str[i+2]!='B')
    	{
    		printf("%c",str[i] );
    		temp=i;
    	}
    		else
    	{
    		i=i+2;
        }

        if(i-temp>=3)
     	{
     		printf(" ");
     	}
}

}