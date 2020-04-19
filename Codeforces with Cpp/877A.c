#include<stdio.h>
#include<string.h>
int main()
{
    char str[100],temp[20],a[]="Shovon";
    int n,i,j,count=0;
    scanf("%s",str);
    n=strlen(str);

    if (strstr(str,a))
        {
            count++;
        }

printf("%d",count);

    return 0;
}
