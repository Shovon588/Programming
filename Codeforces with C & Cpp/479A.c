#include<stdio.h>
#include <string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif
	
int a,b,c,sum1,sum2,sum3,sum4,sum5,sum6;
scanf("%d%d%d",&a,&b,&c);
sum1=a+b+c;
sum2=(a+b)*c;
sum3=a*(b+c);
sum4=a*b*c;
sum5=a+(b*c);
sum6=(a*b)+c;

if(sum1>=sum2 && sum1>=sum3 && sum1 >=sum4 && sum1>=sum5 && sum1>=sum6)
{
printf("%d",sum1);
}
else if(sum2>=sum1 && sum2>=sum3 && sum2 >=sum4 && sum2>=sum5 && sum2>=sum6)
{
printf("%d",sum2);
}
else if(sum3>=sum1 && sum3>=sum2 && sum3>=sum4 && sum3>=sum5 && sum3>=sum6)
{
printf("%d",sum3);
}
else if(sum4>=sum1 && sum4>=sum2 && sum4>=sum3 && sum4>=sum5 && sum4>=sum6)
{
printf("%d",sum4);
}
else if(sum5>=sum1 && sum5>=sum2 && sum5>=sum3 && sum5>=sum4 && sum5>=sum6)
{
printf("%d",sum5);
}
else if(sum6>=sum1 && sum6>=sum2 && sum6>=sum3 && sum6>=sum4 && sum6>=sum5)
{
printf("%d",sum6);
}
}