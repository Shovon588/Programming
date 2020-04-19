#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

long long int d1,d2,d3,way[4],temp,j,i;
scanf("%lld%lld%lld",&d1,&d2,&d3);

way[0]=2*(d1+d2);
way[1]=2*(d2+d3);
way[2]=2*(d1+d3);
way[3]=d1+d2+d3;

for(i=0;i<4;i++)
{
	for(j=0;j<4;j++)
	{
		if(way[i]<way[j])
		{
			temp=way[i];
			way[i]=way[j];
			way[j]=temp;
		}
	}

}

printf("%lld\n",way[0] );

}