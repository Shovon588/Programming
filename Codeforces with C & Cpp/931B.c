#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,a,b,i,count=1,x=0,check;

    scanf("%d%d%d",&n,&a,&b);
    check=n;

    int arr[256]={0};

    arr[a]=a;
    arr[b]=b;

    while(n>1)
    {
    	for(i=0;i<n;i++)
    	{
    		if((arr[i]==a && arr[i+1]==b) || arr[i]==b && arr[i+1]==a)
    		{
    			x=1;
    			break;
    		}

    		else
    		{
    			if(arr[i]==a && arr[i]%2==0)
    			{
    				a=a/2;
    				arr[a]=a;
    			}
    			else if(arr[i]==a && arr[i]%2!=0)
    			{
    				a=(a/2)+1;
    				arr[a]=a;
    			}
    			else if(arr[i]==b && arr[i]%2==0)
    			{
    				b=b/2;
    				arr[b]=b;
    			}
    			else if(arr[i]==b && arr[i]%2!=0)
    			{
    				b=(b/2)+1;
    				arr[b]=b;
    			}
    		}
    	}

    	if(x==1)
    	{
    		break;
    	}

    	count++;
    	n=n/2;


    }


    if(check==2 && count==1)
    {
    	printf("Final!\n");
    }
    else if(check==4 && count==2)
    {
    	printf("Final!\n");
    }
    else if(check==8 && count==3)
    {
    	printf("Final!\n");
    }
    else if(check==16 && count==4)
    {
    	printf("Final!\n");
    }
    else if(check==32 && count==5)
    {
    	printf("Final!\n");
    }
    else if(check==64 && count==6)
    {
    	printf("Final!\n");
    }
    else if(check==128 && count==7)
    {
    	printf("Final!\n");
    }
    else if(check==256 && count==8)
    {
    	printf("Final!\n");
    }
    else
    {
    	printf("%d\n",count );
    }


}



