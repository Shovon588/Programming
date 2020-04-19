#include<stdio.h>
#include<string.h>
int main()
{

    char str[100];
    int a;
  	scanf("%[^\n]s",str);
  	a=strlen(str);

  	if(a==16)
  	{
  		printf("Byangette\n" );
  	}
  	else
  	{
  		printf("Byang\n");
  	}


    return 0;
}