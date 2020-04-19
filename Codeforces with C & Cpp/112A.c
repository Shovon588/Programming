#include<stdio.h>
#include <string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

char a[100],b[100];
int n,i,count=0;
scanf("%s%s",a,b);
n=strlen(a);

for(i=0;i<n;i++)
{
	if(a[i]==b[i] || a[i]==b[i]+32 || a[i]==b[i]-32)
	{
		count++;
	}

	else
	{
		if((a[i]>=97 && b[i]>=97) || (a[i]<97 && b[i]<97))
		{
			if(a[i]>b[i])
			{
				printf("1\n");
				break;
			}
			else
			{
				printf("-1\n");
				break;
			}
		}

		else
		{
			if(a[i]>b[i])
			{
				if(a[i]-b[i]>32)
				{
					printf("1\n");
					break;
				}
				else
				{
					printf("-1\n");
					break;
				}
			}
			else
			{
				if(b[i]-a[i]>32)
				{
					printf("-1\n");
					break;
				}
				else
				{
					printf("1\n");
					break;
				}
			}
		}

	}
}


if(count==n)
{
	printf("0\n");
}

}