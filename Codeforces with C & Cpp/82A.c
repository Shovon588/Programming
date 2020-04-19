#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    long long int n;
   	char a[][9]={"Sheldon","Leonard","Penny","Rajesh","Howard"};
    scanf("%lld",&n);

    while(n>5)
    {
    	n=n/2-2;
    }
    puts(a[n-1]);

}