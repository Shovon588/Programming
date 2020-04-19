#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    
    int left,right,a,temp,answer;
    scanf("%d%d%d",&left,&right,&a);

    if(left==right)
    {
    	temp=a/2;
    	answer=(2*left)+(2*temp);
    }
    else if(right>left)
    {
    	while(left<right && a>0)
    	{
    		left++;
    		a--;
    	}

    	temp=a/2;
    	answer=(2*left)+(2*temp);
    }
    else if(left>right)
    {
    	while(right<left && a>0)
    	{
    		right++;
    		a--;
    	}
    	temp=a/2;
    	answer=(2*right)+(2*temp);
    }

    printf("%d\n",answer );

   

}