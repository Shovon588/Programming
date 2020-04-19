#include<stdio.h>
#include <string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

long long int n;
int temp,newn=0,rem,demp,cemp,newnn=0;
scanf("%I64d",&n);

temp=n;
while(temp!=0)
{
rem=temp%10;
newn=newn*10+rem;
temp=temp/10;
}

if (newn==n)
{
printf("YES");
}

else if(newn!=n)
{
demp=n;
while(demp%10==0)
{
demp=demp/10;
}

cemp=demp;

while(cemp!=0)
{
rem=cemp%10;
newnn=newnn*10+rem;
cemp=cemp/10;
}

if(newnn==demp)
{
printf("YES");
}
else
{
printf("NO");
}
}



}