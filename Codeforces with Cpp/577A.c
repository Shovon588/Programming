#include<stdio.h>
int main()
{
  #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
  #endif

    long long int a,b,check;
    int i,j,count=0;
    scanf("%lld%lld",&a,&b);

    for(i=1;i<=a;i++)
    {
        if(b%i==0 && b/i<=a)
        {
          count++;
        }
    }


    printf("%d",count);


    return 0;
}
