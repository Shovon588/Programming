#include<bits/stdc++.h>
using namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int a[26],i,l,c;
    char str[11];

    for(i=0;i<26;i++)
    {
        scanf("%d",&a[i]);
    }
    scanf("%s",str);
    l=strlen(str);
    int b[l];

    for(i=0;i<l;i++)
    {
        c=str[i];
        b[i]=a[c-97];
    }
    sort(b,b+l);

    printf("%d\n",b[l-1]*l );
}