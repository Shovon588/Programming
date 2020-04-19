#include<stdio.h>
#include<string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    char str[1000],arr[1000];
    int a,i,j=0,k,count=0;

    scanf("%[^\n]s",str);

    a=strlen(str);

    for(i=0;i<a;i++)
    {
    	if(str[i]>=97 && str[i]<=122)
    	{
    		arr[j]=str[i];
    		j++;
    	}
    }
    
    for(i=0;i<j;i++)
  	{
  		for(k=i+1;k<j;k++)
  		{
  			if(arr[i]==arr[k])
  			{
  				count++;
  				break;
  			}
  		}
  	}

  	printf("%d\n",j-count);

}