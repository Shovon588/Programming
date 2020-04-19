#include<stdio.h>
#include<string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

	char str[100];
	int i,count=0,l;
	scanf("%s",str);
	l=strlen(str);

	for(i=0;i<l;i++)
	{
		if(str[i]=='a' || str[i]=='e' || str[i]=='i' || str[i]=='o' || str[i]=='u')
		{
			count++;
		}
		else if(str[i]>=48 && str[i]<=57)
		{
			if(str[i]%2!=0)
			{
			count++;
			}
		}
	}

	printf("%d\n",count );



	return 0;
}