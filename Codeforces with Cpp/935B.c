#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,i,count=0,up,down,gate,x=0,y=0;
    scanf("%d",&n);

    char str[n];
    scanf("%s",str);

   	if(str[0]=='U')
   	{
   		y++;
   		up=1;
   		down=0;
   		gate=0;
   		count=0;
   	}
   	else
   	{
   		x++;
   		up=0;
   		down=1;
   		gate=0;
   		count=0;
   	}


   	for(i=1;i<n;i++)
   	{

   		if(str[i]=='U')
   		{
   			y++;
   		}
   		else
   		{
   			x++;
   		}

   		if(x>y)
   		{
   			up=0;
   			down=1;
   			gate=0;
   		}
   		else if(y>x)
   		{
   			up=1;
   			down=0;
   			gate=0;
   		}
   		else
   		{
   			gate=1;
   		}

   		

   		if(gate==1 && up==1 && str[i+1]=='R')
   		{
   			count++;
   		}
   		else if(gate==1 && down==1 && str[i+1]=='U')
   		{
   			count++;
   		}

   		
   	}

   	printf("%d\n",count );


   	

}