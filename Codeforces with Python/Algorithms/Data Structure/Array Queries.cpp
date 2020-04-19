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
       ll t,n,m,i,j,x,y,temp;
       scanf("%lld",&t);

       for(i=0;i<t;i++){
              scanf("%lld%lld",&n,&m);
              ll a[n];
              ll tree[3*n]={0};

              for(j=0;j<n;j++){
                     scanf("%lld",&a[j]);
              }
              segTree(1,0,n-1,a,tree);

              printf("Case %lld:\n",i+1);

              for(j=0;j<m;j++){
                     scanf("%lld%lld",&x,&y);
                     temp=query(1,1,n,x,y,a,tree);
                     printf("%lld\n",temp);
              }

       }


       return 0;
}
