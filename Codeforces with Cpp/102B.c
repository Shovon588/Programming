#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

long long int n,i,count=0;
scanf("%lld",&n);
int temp2,temp=0;


while(n>0)
{
	temp=0;
	temp2=n;

	while(temp2>0)
	{
		temp=temp+(temp2%10);
		temp2=temp2/10;
	}
	count++;
	n=temp;
	printf("%d\n",temp );

}
printf("%lld\n",count );


}