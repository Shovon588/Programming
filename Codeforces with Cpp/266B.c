#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,t,i,j;
    scanf("%d%d",&n,&t);

    char str[n];
    scanf("%s",str);

    for(i=0;i<t;i++)
    {
    	for(j=0;j<n;j++)
    	{
    		if(str[j]=='B' && str[j+1]=='G')
    		{
    			str[j+1]='B';
    			str[j]='G';
    			j++;
    		}
    	}
    }

    printf("%s\n",str );


}