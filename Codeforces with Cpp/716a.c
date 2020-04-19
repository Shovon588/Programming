#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif


long long int n,t,i,time=0,temp,count=0,check=0;
scanf("%lld%lld",&n,&t);
long long int a[n];
for(i=0;i<n;i++)
{
	scanf("%lld",&a[i]);

	temp=a[i]-time;
	time=a[i];

	if(temp>t)
	{
		count=0;
		check++;
	}
	else
	{
		count++;
	}
}

if(check==0)
{
	printf("%lld\n",count );
}
else
{
	printf("%lld\n",count+1 );
}

}