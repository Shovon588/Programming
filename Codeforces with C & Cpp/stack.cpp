#include<bits/stdc++.h>
using namespace std;
int main()
{
    char str[100];
    char temp[100];

    scanf("%s",str);

    int len=strlen(str);
    int j=-1;

    for(int i=0;i<len;i++)
    {
        if(str[i]=='(' || str[i]=='{')
        {
            j++;
            temp[j]=str[i];
        }
        else if(str[i]==')' || str[i]=='}')
        {
            if((temp[j]=='(' && str[i]==')') || (temp[j]=='{' && str[i]=='}') )
            {
                j--;
            }
        }
        printf("%s\n",temp);

    }




    return 0;
}
