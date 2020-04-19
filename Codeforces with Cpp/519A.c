#include<stdio.h>
int main()
{
  #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
  #endif


    char str[71];
    int i,black=0,white=0;

    for(i=0;i<71;i++)
    {
        scanf("%c",&str[i]);

        if(str[i]=='Q')
        {
            white=white+9;
        }
        else if(str[i]=='R')
        {
            white=white+5;
        }
        else if(str[i]=='B')
        {
            white=white+3;
        }
        else if(str[i]=='N')
        {
          white=white+3;
        }
        else if(str[i]=='P')
        {
          white=white+1;
        }


        else if(str[i]=='q')
        {
            black=black+9;
        }
        else if(str[i]=='r')
        {
            black=black+5;
        }
        else if(str[i]=='b')
        {
            black=black+3;
        }
        else if(str[i]=='n')
        {
          black=black+3;
        }
        else if(str[i]=='p')
        {
            black=black+1;
        }
    }


    if(black>white)
    {
      printf("Black\n");
    }
    else if(white>black)
    {
      printf("White\n");
    }
    else
    {
      printf("Draw\n");
    }
}
