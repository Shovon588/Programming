#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif


    int n,d,i,a,sum=0,jokestime,jokes,dif;
    scanf("%d%d",&n,&d);
    for(i=0;i<n;i++)
    {
    	scanf("%d",&a);
    	sum=sum+a;
    }

    jokestime=(n-1)*10;
    jokes=(jokestime/5);
    dif=d-(sum+jokestime);

  	if(dif>=0)
  	{
  		if(sum+jokestime<=d)
  		{
  			printf("%d\n",jokes+(dif/5) );
  		}
  		else
  		{
  			printf("-1\n");
  		}
  	}
  	else
  	{
  		printf("-1\n");
  	}



}