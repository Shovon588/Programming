#include<bits/stdc++.h>
using namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    char ch,a='a',b='b',c='c',d='d',e='e',f='f',g='g',h='h',i='i',blank;
    int j;

    printf("X for player 1 | 0 for player\n\n");
    printf("%c 	|	b 	|	c\nd	|	e 	|	f\ng	|	h	|	i\n\n",a);



    for(j=1;j<=9;j++)
    {
   	if(j%2!=0)
   	{
   	printf("Player 1s turn!\nPlease select a cell where there is no X or 0\n\n");
   	printf("%c 	|	%c 	|	%c\n%c	|	%c 	|	%c\n%c	|	%c	|	%c\n\n",a,b,c,d,e,f,g,h,i);
   	scanf("%c%c",&ch,&blank);

   	if(ch=='a')
   	{
    	a='X';
   	}
   	else if(ch=='b')
   	{
   		b='X';
   	}
   	else if(ch=='c')
   	{
   		c='X';
   	}
   	else if(ch=='d')
   	{
   		d='X';
   	}
   	else if(ch=='e')
   	{
   		e='X';
   	}
   	else if(ch=='f')
   	{
   		f='X';
   	}
   	else if(ch=='g')
   	{
   		g='X';
   	}
   	else if(ch=='h')
   	{
   		h='X';
   	}
   	else if(ch=='i')
   	{
   		i='X';
   	}
   	
   	}

   	else
   	{
   	printf("Player 2s turn\nPlease select a cell where there is no X or 0\n\n");
   	printf("%c 	|	%c 	|	%c\n%c	|	%c 	|	%c\n%c	|	%c	|	%c\n\n",a,b,c,d,e,f,g,h,i);
   	scanf("%c%c",&ch,&blank);

   	if(ch=='a')
   	{
    	a='0';
   	}
   	else if(ch=='b')
   	{
   		b='0';
   	}
   	else if(ch=='c')
   	{
   		c='0';
   	}
   	else if(ch=='d')
   	{
   		d='0';
   	}
   	else if(ch=='e')
   	{
   		e='0';
   	}
   	else if(ch=='f')
   	{
   		f='0';
   	}
   	else if(ch=='g')
   	{
   		g='0';
   	}
   	else if(ch=='h')
   	{
   		h='0';
   	}
   	else if(ch=='i')
   	{
   		i='0';
   	}
   	
   	}


   	if((c=='X' && e=='X' && g=='X') || (a=='X' && e=='X' && i=='X') || (b=='X' && e=='X' && h=='X') || (d=='X' && e=='X' && f=='X'))
   	{
   		printf("Player 1 wins!\n");
   		break;
   	}
   	else if((c=='0' && e=='0' && g=='0') || (a=='0' && e=='0' && i=='0') || (b=='0' && e=='0' && h=='0') || (d=='0' && e=='0' && f=='0'))
   	{
   		printf("Player 2 wins!\n");
   		break;
   	}
}
}