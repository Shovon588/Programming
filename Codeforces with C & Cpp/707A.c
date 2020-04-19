#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,m,i,j,count=0,total;
    scanf("%d%d",&n,&m);
    total=n*m;
    char c[5];

    for(i=0;i<(total);i++)
    {
    	scanf("%s",c);
    	
    	if(c[0]=='C'|| c[0]=='M' || c[0]=='Y')
    	{
    		count++;
    	}
    }


    if(count>0)
    {
    	printf("#Color\n");
    }
    else if(count==0)
    {
    	printf("#Black&White\n");
    }
}

