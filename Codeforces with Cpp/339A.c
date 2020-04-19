#include<stdio.h>
#include <string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    char str[100];
    int i,j;
    char temp;
    scanf("%s",str);
    for(i=0;i<strlen(str);i=i+2)
    {
        for(j=i+2;j<strlen(str);j=j+2)
        {
            if(str[i]>=str[j])
            {
            temp=str[i];
            str[i]=str[j];
            str[j]=temp;
            }
        }
    }
    printf("%s",str);

}