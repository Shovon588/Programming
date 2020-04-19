#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

int n,p,i,q,j,k,size;
scanf("%d%d",&n,&p);
int a[p];

for(i=0;i<p;i++)
{
	scanf("%d",&a[i]);
}
scanf("%d",&q);
int b[q];

for(i=0;i<n;i++)
{
	scanf("%d",&b[i]);
}
size=p+q;

int c[size];
i=j=k=0;

while(i<p && j<q)
{
	if(a[i]<=b[j])
	{
		c[k]=a[i];
		i++;
		k++;
	}
	else
	{
		c[k]=b[j];
		j++;
		k++;
	}
}
while(i<p)
{
	c[k]=a[i];
	i++;
	k++;
}

while(j<q)
{
	c[k]=b[j];
	j++;
	k++;
}

for(i=0;i<size;i++)
{
	for(j=i+1;j<size;)
	{
		if(c[j]==c[i])
		{
			for(k=j;k<size;k++)
			{
				c[k]=c[k+1];
			}
			size--;
		}
		else
		{
			j++;
		}
	}
}

if(size==n)
{
	printf("I become the guy.\n");
}
else
{
	printf("Oh, my keyboard!\n");
}

}