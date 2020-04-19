#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

int n,m,i,j,k;
scanf("%d%d",&n,&m);

for(i=1;i<=n;i++)
{
if(i%2!=0)
{
for(j=0;j<m;j++)
{
printf("#");
}
printf("\n");
}

else
{
if(i%4!=0)
{
for(k=1;k<=m;k++)
{
if(k==m)
{
printf("#");
}
else
{printf(".");}
}
printf("\n");
}
else{
for(k=1;k<=m;k++)
{
if(k==1)
{
printf("#");
}
else
{printf(".");}
}
printf("\n");
}
}

}

return 0;
}