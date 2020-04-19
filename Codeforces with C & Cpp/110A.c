#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    long long int n,temp,count=0;
    scanf("%lld",&n);


    while(n!=0)
    {
    	temp=n%10;
    	if(temp==4 || temp==7)
    	{
    		count++;
    	}
    	n=n/10;
    }



    if(count==4 || count==7)
    {
    	printf("YES\n");
    }
    else
    {
    	printf("NO\n");
    }

    



}