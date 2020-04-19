#include<stdio.h>
int main()
{
  #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
  #endif
    
int a[5][5],i,j,row,column,count=0;
for(i=0;i<5;i++)
{
for(j=0;j<5;j++)
{
scanf("%d",&a[i][j]);
}
}

for(i=0;i<5;i++)
{
for(j=0;j<5;j++)
{
if(a[i][j]==1)
{
row=i+1;
column=j+1;
while(row!=3)
{
if(row<3)
{row=row+1;count=count+1;}
else{row=row-1;count=count+1;}
}

while(column!=3)
{
if(column<3)
{column=column+1;count=count+1;}
else{column=column-1;count=count+1;}
}
}
}
}
printf("%d",count);


return 0;
}
