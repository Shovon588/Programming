#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

int n,t,a,count=1,i,temp;
scanf("%d%d",&n,&t);

for(i=0;i<n;i++)
{
scanf("%d",&a);

temp=86400-a;
if(temp>=t)
{
printf("%d",count);
break;
}
else
{
count++;
t=t-temp;
}

}


}