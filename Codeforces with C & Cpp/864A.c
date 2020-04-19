#include<stdio.h>
#include <string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

int n,i,j,b,c,d,count=0,countb=0;
scanf("%d",&n);
int a[n],e;
for(i=0;i<n;i++)
{
scanf("%d",&a[i]);
}

b=a[0];

for(i=0;i<n;i++)
{
for(j=0;j<i;j++)
{
if(a[i]==a[j])
break;
}
if(i==j)
{
count++;
}
}

if(count==2)
{
for(i=1;i<n;i++)
{
if(b==a[i])
{
countb++;
}
else{
e=a[i];
}
}
c=countb+1;

if(n-c==c)
{
printf("YES\n%d %d",a[0],e);
}
else
{
printf("NO");
}
}


else
{
printf("NO");
}



}