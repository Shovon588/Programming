#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,m,i,a,b,j;
    scanf("%d%d",&n,&m);
    char str[n];
    char c1,c2,g;
    int l[m],r[m];

    scanf("%s",str);
    
    for(i=0;i<m;i++)
    {
    	scanf("%d%d",&l[i],&r[i]);
    	scanf("%c",&g);
    	scanf("%c%c%c",&c1,&g,&c2);

    	a=l[i];
    	b=r[i];

    	for(j=a-1;j<b;j++)
    	{
    		
    		if(str[j]==c1)
    		{
    			str[j]=c2;
    		}
    	}

    }

    printf("%s\n",str );
}