#include<stdio.h>
#include<string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    char str[1000];
    int i,modfour,modhun,modfourhun,j,l;

    while(scanf("%s",str)==1)
    {
    	modfour=0;
    	modhun=0;
    	modfourhun=0;
    	l=strlen(str);

    	for(i=0;i<l;i++)
    	{
    		modfour=((modfour*10)+str[i]-'0')%4;
    		modhun=((modhun*10)+str[i]-'0')%100;
    		modfourhun=((modfourhun*10)+str[i]-'0')%400;
    	}

    	printf("%d\n",l );
    	if((modfour==0 && modhun!=0) || modfourhun==0)
    	{
    		printf("Leap year\n");
    	}
    	else
    	{
    		printf("Not a leap year\n");
    	}
    }
}