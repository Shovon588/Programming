#include<stdio.h>
#include<string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif


    char a[200], b[200];

    int i,j,cry=0,k=0,x[200],y[200],sum[200],len_a,len_b,c=0,count=0;

    printf("Enter 1st number: ");

    scanf("%s",a);
    len_a=strlen(a);

    printf("Enter 2nd number: ");

    scanf("%s",b);
    len_b=strlen(b);

    for(i=0; a[i]!='\0'; i++)
    {
        x[i]=a[i]-'0';
    }
    printf("\n");
    for(j=0; b[j]!='\0'; j++)
    {
        y[j]=b[j]-'0';
    }
    printf("\n");


    for(i=len_a-1,j=len_b-1; i>=0,j>=0; i--,j--)
    {

        if((x[i]+y[j]+cry)>=10)
        {
            if(i==0 && j==0 )
            {
                sum[k]=(x[i]+y[j]+cry);
                k++;
            }
            if(i!=0 || j!=0)
            {
                sum[k]=(x[i]+y[j]+cry)%10;
                cry=(x[i]+y[j]+cry)/10;
                k++;
            }


        }
        else
        {

            sum[k]=(x[i]+y[j]+cry)%10;
            cry=0;
            k++;

        }
        if(i==0&&j!=0||i!=0&&j==0)
        {
            if(i==0)
            {
                x[i]=0;

                i++;
            }
            else
            {
                y[j]=0;

                j++;
            }
        }

    }
    printf("\n");

    for(i=k-1; i>=0; i--)
    {
        if(sum[i]==0 && c==0)
        {
        	count++;
            continue;
        }
        else
        {
            printf("%d",sum[i]);
            c++;
        }

       
    }
        if(count==k)
        {
        	printf("0\n");
        }

    return 0;



}