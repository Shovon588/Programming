#include<stdio.h>
#include<string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    long long int k,p;
    int i=10,a,n=0;
    char str[10];

    scanf("%lld%lld",&k,&p);

    	while(n<k)
    	{
    	sprintf(str,"%d",i);
    	a=strlen(str);

    	if(a%2==0)
    	{
    		if(str[0]==str[a-1])
    		{
    			printf("%d\n",a );
    			n++;
    			i++;
    		}
    	}
    }  
}