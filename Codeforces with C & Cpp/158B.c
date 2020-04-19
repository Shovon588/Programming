#include<stdio.h>
#include <string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

long long int n;
int i,count=0,one=0,two=0,three=0,temp;
scanf("%lld",&n);
int a[n];
for(i=0;i<n;i++)
{
scanf("%d",&a[i]);
if(a[i]==4)
{count++;}
else if(a[i]==3)
{three++;}
else if(a[i]==2)
{two++;}
else
{one++;}
}

if(three==one)
{
count=count+three;
three=0;
one=0;
}
else if(three!=one)
{
if(three>one)
{three=three-one;
count=count+one;
one=0;
}
else if(one>three)
{one=one-three;
count=count+three;
three=0;
}
}

if(three>0)
{count=count+three;three=0;}

if(two>=2 && two%2==0)
{
count=count+(two/2);
two=0;
}
else if(two>2 && two%2!=0)
{
count=count+(two-1)/2;
two=1;
}

temp=(two*2)+one;

if(temp>0 && temp<=4)
{count=count+1;
two=0;one=0;}
else if(temp>4 && temp%4==0)
{
count=count+temp/4;
two=0;one=0;
}
else if(temp>4 && temp%4!=0)
{
count=count+(temp/4)+1;
two=0;one=0;
}
printf("%d\n",count);


}