#include <bits/stdc++.h>
using  namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif


    int n;
    char s1[100],s2[100];

    scanf("%d %s %s",&n,s1,s2);

    if(s2[0]=='m')
    {
        if(n>=1 && n<=29)
        {
            printf("12\n");
        }
        else if(n==30)
        {
            printf("11\n");
        }
        else if(n==31)
        {
            printf("7\n");
        }
    }
    else if(s2[0]=='w')
    {
        if(n==1 || n==2)
        {
            printf("51\n");
        }
        else
        {
            printf("52\n");
        }
    }

}

