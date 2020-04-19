#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,i,t,j;
    scanf("%d",&t);
    long long int initial,final,a,total=0;
    char str[1000];

    for(i=0;i<t;i++)
    {
    	scanf("%lld%lld",&initial,&final);
    	scanf("%d",&n);

    	for(j=0;j<n;j++)
    	{
    		scanf("%s%lld",str,&a);

    		if(str[0]=='i' && str[1]=='n')
    		{
    			total=total+a;
    		}
    		else
    		{
    			total=total-a;
    		}
    	}

    	if(total+initial==final)
    	{
    		printf("yes\n");
    	}
    	else{
    		printf("no\n");
    	}

    	total=0;

    }


}