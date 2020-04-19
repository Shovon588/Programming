#include<stdio.h>
#include<string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

char str1[200],str2[200];
int a,b,i,j,carry=0,k,num1[200],num2[200],sum[200];

scanf("%s%s",str1,str2);
a=strlen(str1);
b=strlen(str2);

for(i=0;i<a;i++)
{
	num1[i]=str1[i]-'0';
}
for(i=0;i<b;i++)
{
	num2[i]=str2[i]-'0';
}

k=0;


// Jokhon duita number e same size er hobe...mane dhoren 1000+4483 sei khetre

if(a==b)
{
for(i=a-1,j=b-1;i>=0,j>=0;i--,j--)
{
	sum[k]=num1[i]+num2[j]+carry;

	if(sum[k]>=10)
	{
		carry=sum[k]/10;
		sum[k]=sum[k]%10;
		k++;
	}
	else
	{
		sum[k]=sum[k];
		carry=0;
		k++;
	}
}

if(carry>0)
{
printf("%d",carry );
}

for (i=k-1;i>=0;i--)
{
	printf("%d",sum[i] );
}
}

//jokhon prothom number er size boro hobe...mane dhoren 1000+23 sei khetre

if (a>b)
{
	for(i=b-1,j=a-1;i>=0;i--,j--)
	{
		sum[k]=num2[i]+num1[j]+carry;

		if(sum[k]>=10)
		{
			carry=sum[k]/10;
			sum[k]=sum[k]%10;
			k++;
		}
		else
		{
			sum[k]=sum[k];
			carry=0;
			k++;
		}
	}

for(i=a-b-1;i>=0;i--)
{
	sum[k]=num1[i]+carry;
	if(sum[k]>=10)
		{
			carry=sum[k]/10;
			sum[k]=sum[k]%10;
			k++;
		}
		else
		{
			sum[k]=sum[k];
			carry=0;
			k++;
		}
}

for(i=k-1;i>=0;i--)
{
	printf("%d",sum[i] );
}

}


//jokhon prothom number er size boro hobe...mane dhoren 23+1000 sei khetre

if(a<b)
{
		for(i=a-1,j=b-1;i>=0;i--,j--)
	{
		sum[k]=num1[i]+num2[j]+carry;
		if(sum[k]>=10)
		{
			carry=sum[k]/10;
			sum[k]=sum[k]%10;
			k++;
		}
		else
		{
			sum[k]=sum[k];
			carry=0;
			k++;
		}
	}

for(i=b-a-1;i>=0;i--)
{
	sum[k]=num2[i]+carry;

	if(sum[k]>=10)
		{
			carry=sum[k]/10;
			sum[k]=sum[k]%10;
			k++;
		}
		else
		{
			sum[k]=sum[k];
			carry=0;
			k++;
		}

}
for(i=k-1;i>=0;i--)
{
	printf("%d",sum[i] );
}
}



}