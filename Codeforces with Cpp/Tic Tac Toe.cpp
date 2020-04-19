#include<bits/stdc++.h>
using namespace std;
int main()
{

    char ch,a='a',b='b',c='c',d='d',e='e',f='f',g='g',h='h',i='i',blank,button='y';
    int j,x;

    printf("Before starting you have to keep something in your mind.\n1. You can not select a cell where there is already a X or 0\n");
    printf("2. You just have to type the character in which cell you wanna put your mark.\n3. You can only choose a character between (a-i)\n\n");

    printf("Now we are good to go\n\n");



    while(button=='y')
    {
    for(j=1;j<=9;j++)
    {
   	if(j%2!=0)
   	{
    printf("Player 1s turn\n\n");
   	printf("    %c 	|	%c 	|	%c\n    %c	|	%c 	|	%c\n    %c	|	%c	|	%c\n\n",a,b,c,d,e,f,g,h,i);
   	printf("Type any remaining character and hit enter=");
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
   	printf("\n\nPlayer 2s turn\n\n");
   	printf("    %c 	|	%c 	|	%c\n    %c	|	%c 	|	%c\n    %c	|	%c	|	%c\n\n",a,b,c,d,e,f,g,h,i);
   	printf("Type any remaining character and hit enter=");
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


   	if((c=='X' && e=='X' && g=='X') || (a=='X' && e=='X' && i=='X') || (b=='X' && e=='X' && h=='X') || (d=='X' && e=='X' && f=='X') || (a=='X' && d=='X' && g=='X') || (c=='X' && f=='X' && i=='X') || (a=='X' && b=='X' && c=='X') || (g=='X' && h=='X' && i=='X'))
   	{
   		printf("\n\nPlayer 1 wins!\n");
   		x=1;
   		printf("%c 	|	%c 	|	%c\n%c	|	%c 	|	%c\n%c	|	%c	|	%c\n\n",a,b,c,d,e,f,g,h,i);
   		break;
   	}
   	else if((c=='0' && e=='0' && g=='0') || (a=='0' && e=='0' && i=='0') || (b=='0' && e=='0' && h=='0') || (d=='0' && e=='0' && f=='0') || (a=='X' && d=='X' && g=='X') || (c=='X' && f=='X' && i=='X') || (a=='X' && b=='X' && c=='X') || (g=='X' && h=='X' && i=='X'))
   	{
   		printf("\n\nPlayer 2 wins!\n");
   		x=1;
   		printf("%c 	|	%c 	|	%c\n%c	|	%c 	|	%c\n%c	|	%c	|	%c\n\n",a,b,c,d,e,f,g,h,i);
   		break;
   	}
}
if(x!=1)
{
    printf("\n\nMatch drawn!");
}
printf("\n\nWanna play again ? y/n\n");
scanf("%c%c",&button,&blank);
if(button=='y')
{
    a='a',b='b',c='c',d='d',e='e',f='f',g='g',h='h',i='i';
}

}
}
