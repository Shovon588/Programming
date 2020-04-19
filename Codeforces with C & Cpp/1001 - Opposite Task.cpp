#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
int main()
{
       ll t,a,i;
       scanf("%lld",&t);
       for(i=0;i<t;i++){
              scanf("%lld",&a);
              if (a<=10){
                     printf("0 %lld\n",a);
              }
              else if(a>10){
                     printf("10 %lld\n",a-10);
              }
       }



       return 0;
}
