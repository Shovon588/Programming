#include<stdio.h>
#include <string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

long long int a,result;
scanf("%lld",&a);

if(a%2==0)
{
	result=a/2;
	printf("%lld\n",result );
} 
else
{
	result=(a/2)+1;
	printf("%lld\n",-result );
}


}