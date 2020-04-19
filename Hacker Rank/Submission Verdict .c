#include<bits/stdc++.h>
using namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,i;
    char str[100];
    scanf("%d",&n);

    for(i=0;i<n;i++)
    {
        scanf("%s",str);

        if(str[0]=='a' && str[1]=='c')
        {
            printf("Accepted\n");
        }
        else if(str[0]=='w' && str[1]=='a')
        {
            printf("Wrong Answer\n");
        }
        else if(str[0]=='r' && str[1]=='t' && str[2]=='e')
        {
            printf("Run Time Error\n");
        }
        else if(str[0]=='t' && str[1]=='l' && str[2]=='e')
        {
            printf("Time Limit Exceeded\n");
        }
    }
}