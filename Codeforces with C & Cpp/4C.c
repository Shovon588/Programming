#include<stdio.h>
#include<string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif


    int n,i,sum=0,len;
    scanf("%d",&n);
    char str[32];
    for(i=0;i<n;i++)
    {
    	scanf("%s",str);
    	len=strlen(str);

    printf("sum=%d\n",sum );

    }


    for(i=0;i<n;i++)
    {
    	len=strlen(str[i]);
    	for(i=0;i<len;i++)
    	{
    		sum=sum+str[i];
    	}
}