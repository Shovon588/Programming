#include<bits/stdc++.h>
using namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,i,l,count=0,j;
    scanf("%d",&n);
    char a[10005],c;

    for(i=0;i<n;i++)
    {
        count=0;
        scanf(" %[^\n]s",a);
        l=strlen(a);

        for(j=0;j<l;j++)
        {
            if((a[j]=='p'|| a[j]=='P') && (a[j+1]=='r' || a[j+1]=='R') && (a[j+2]=='o' || a[j+2]=='O') && (a[j+3]=='b' || a[j+3]=='B') && (a[j+4]=='l' || a[j+4]=='L') && (a[j+5]=='e' || a[j+5]=='E') && (a[j+6]=='m' || a[j+6]=='M') && (a[j+7]!='s' || a[j+7]!='S'))
            {
                count++;
            }
            else if((a[j]=='p'|| a[j]=='P') && (a[j+1]=='r' || a[j+1]=='R') && (a[j+2]=='o' || a[j+2]=='O') && (a[j+3]=='b' || a[j+3]=='B') && (a[j+4]=='l' || a[j+4]=='L') && (a[j+5]=='e' || a[j+5]=='E') && (a[j+6]=='m' || a[j+6]=='M') && (a[j+7]=='.' || a[j+7]=='!' || a[j+7]=='?' || a[j+7]==',') && (a[j+8]!='.' || a[j+8]!=',' || a[j+8]!='?' || a[j+8]!='!'))
            {
                count++;
            }
        }


        if(count>0)
        {
            printf("Case %d: %d problems\n",i+1,count );
        }
        else
        {
            printf("Case %d: No problem\n",i+1);
        }

    }
}