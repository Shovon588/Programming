#include<bits/stdc++.h>
using namespace std;
int main()
{
       int n,k,i,j,flag;
       scanf("%d%d",&n,&k);

       if (2*k>=n)
       {
              printf("-1");
       }
       else
       {
              printf("%d\n",n*k);
              for(i=1;i<=n;i++)
              {
                     flag=i+1;
                     for(j=0;j<k;j++)
                     {
                            if (flag>n)
                            {
                                   flag=1;
                            }
                            printf("%d %d\n",i,flag);
                            flag++;
                     }
              }
       }


       return 0;
}
