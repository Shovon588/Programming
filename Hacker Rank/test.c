#include<stdio.h>
#include<math.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    long long int a,b,c,d,e;
    a=865;
    b=107;
    c=970686; d=723490; e=741673;

    printf("%lld\n",(a*c)+(b*d) );
    printf("%lld\n",a*e );
    printf("%lld\n",b*d );

}