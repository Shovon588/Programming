#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;

ll segTree(ll node,ll low,ll high,ll a[],ll tree[])
{
       if(low==high)
       {
              tree[node]=a[low];
              return tree[node];
       }
       ll left=2*node;
       ll right=(2*node)+1;
       ll mid=(low+high)/2;

       segTree(left,low,mid,a,tree);
       segTree(right,mid+1,high,a,tree);
       tree[node]=min(tree[left],tree[right]);
}

ll query(ll node,ll low,ll high,ll i,ll j,ll a[],ll tree[])
{
       if(j<low || i>high)
       {
              return INT_MAX;
       }
       if (low>=i && high<=j){
              return tree[node];
       }

       ll left=2*node;
       ll right=(2*node)+1;
       ll mid=(high+low)/2;

       ll q1=query(left,low,mid,i,j,a,tree);
       ll q2=query(right,mid+1,high,i,j,a,tree);

       return min(q1,q2);
}


int main()
{
       ll t,n,i,j;
       scanf("%lld",&t);

       for(i=0;i<t;i++)
       {
              scanf("%lld",&n);
              ll a[n];
              ll tree[3*n]={0};
              ll in,b=INT_MAX;


              for(j=0;j<n;j++)
              {
                     scanf("%lld",&a[j]);
                     if(a[j]<b){
                            b=a[j];
                            in=j;
                     }
              }

              segTree(1,0,n-1,a,tree);

              ll q1=INT_MAX,q2=INT_MAX;
              if (in==0)
              {
                    q1=query(1,0,n-1,1,n-1,a,tree);
              }
              else if(in==n-1)
              {
                     q2=query(1,0,n-1,0,n-2,a,tree);
              }
              else
              {
                     q1=query(1,0,n-1,0,in-1,a,tree);
                     q2=query(1,0,n-1,in+1,n-1,a,tree);
                     printf("%lld %lld",q1,q2);
              }

       }




       return 0;
}
