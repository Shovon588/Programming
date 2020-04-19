#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <vector>
#include <map>
#include <string>
#define N  50010
#define rep(i,init,end) for(int i=init;i<end;i++)
#define si(T)   scanf("%d",&T)
#define sii(n,m)    scanf("%d %d",&n,&m)
#define Clear(a)    memset(a,0,sizeof(a))
using namespace std;


int par[N];
int debt[N];
int taka[N];

int find(int a)
{
    if(par[a]==a)   return a;
    return par[a]=find(par[a]);
}
void Union(int a,int b)
{
    if(find(a)!=find(b))    par[find(b)]=find(a);
}
void reset()
{
    Clear(taka);
    Clear(debt);
    rep(i,0,N)  par[i]=i;
}
int main()
{
    int T,CASE=0;
    si(T);
    while(T--)
    {
        reset();
        int n,m;
        sii(n,m);
        rep(i,0,n)  si(debt[i]);
        rep(i,0,m)
        {
            int a,b;
            sii(a,b);
            Union(a,b);
        }
        rep(i,0,n)  taka[find(i)]+=debt[i];
        bool flag=true;
        rep(i,0,n)  if(taka[i]<0)   flag=false;
        if(flag)    puts("POSSIBLE");
        else puts("IMPOSSIBL");
    }
}
