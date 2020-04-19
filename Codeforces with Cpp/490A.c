#include<stdio.h>
int main()
{
  #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
  #endif

   int n,i,a=0,b=0,c=0,j=0,k=0,l=0,small;
   scanf("%d",&n);
   int arra[n],arrb[n],arrc[n],arr[n];

   for(i=0;i<n;i++)
   {
      scanf("%d",&arr[i]);

      if(arr[i]==1)
      {
          a++;
          arra[j]=i+1;
          j++;
      }
      else if(arr[i]==2)
      {
          b++;
          arrb[k]=i+1;
          k++;
      }
      else if(arr[i]==3)
      {
          c++;
          arrc[l]=i+1;
          l++;
      } 

   }

   if(a<=b && a<=c)
   {
      small=a;
   }
   else if(b<=a && b<=c)
   {
      small=b;
   }
   else
   {
      small=c;
   }

   printf("%d\n",small );

   for(i=0;i<small;i++)
   {
      printf("%d %d %d\n",arra[i],arrb[i],arrc[i] );
   }


}
