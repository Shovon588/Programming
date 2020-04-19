#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,k,l,c,d,p,nl,np,totdrink,totslice,totgram,min;
    scanf("%d%d%d%d%d%d%d%d",&n,&k,&l,&c,&d,&p,&nl,&np);

    totdrink=(k*l)/nl;
    totslice=(c*d);
    totgram=(p/np);

    if(totdrink<=totslice && totdrink<=totgram)
    {
    	min=totdrink;
    }
    else if(totslice<=totdrink && totslice<=totgram)
    {
    	min=totslice;
    }
    else if(totgram<=totslice && totgram<=totdrink)
    {
    	min=totgram;
    }

    printf("%d\n",min/n );




}