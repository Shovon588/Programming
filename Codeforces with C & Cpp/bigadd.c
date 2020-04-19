#include<stdio.h>
#include<string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    char a[200], b[200];

    int i,j,cry=0,k=0,x[200],y[200],sum[400],len_a,len_b;

    scanf("%s%s",a,b);

    len_a=strlen(a);

    len_b=strlen(b);


    for(i=0;i<len_a;i++)
    {
        x[i]=a[i]-'0';
    }
  
    for(j=0;j<len_b;j++)
    {
        y[j]=b[j]-'0';
    }

    for(i=len_a-1,j=len_b-1;i>=0 && j>=0;i--,j--)
    {
        if((x[i]+y[j]+cry)>=10)
        {
           sum[k]=(x[i]+y[j]+cry)%10;

           cry=(x[i]+y[j]+cry)/10;

           k++;
        }
        else
        {
            sum[k]=(x[i]+y[j]+cry);
            cry=0;
            k++;
        }

        
        
    }

    if(cry>0)
    {
    printf("%d",cry);
	}

    for(i=k-1;i>=0;i--)
    {
        printf("%d",sum[i]);
    }

}
