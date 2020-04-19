#include<stdio.h>
#include<math.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

	int n,m,a,b;
	scanf("%d%d",&n,&m);

	if(n==1 && m==1)
	{
		printf("2\n");
	}
	else
	{
		if(n>=m)
		{
			a=sqrt(n);
			b=n-(a*a);
			if(((b*b)+a)==m)
			{
				printf("1\n");
			}
			else
			{
				printf("0\n");
			}
		}
		else
		{
			a=sqrt(m);
			b=m-(a*a);
			if(((b*b)+a)==n)
			{
				printf("1\n");
			}
			else
			{
				printf("0\n");
			}
		}
	}


}