#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

   long long int a,b,x,y,z,yellow=0,blue=0;
   scanf("%lld%lld",&a,&b);
   scanf("%lld%lld%lld",&x,&y,&z);

   yellow=(x*2)+(y*1);
   blue=(y*1)+(z*3);

   if(yellow>a)
   {
   		a=yellow-a;
   }
   else{a=0;}

   if(blue>b)
   {
   	b=blue-b;
   }
   else
   {
   	b=0;
   }

   printf("%lld\n",a+b );

}