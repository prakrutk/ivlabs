#include<stdio.h>

void main()
{
	int a[100];
	int i,j,c,max,t,n,sal;
	printf("Enter the lenght of array");
	scanf("%d",&n);
	printf("Enter the array");
	for(i = 0; i < n; i ++)
	{
		scanf("%d",&a[i]);
	}
	i=0;
	c=0;
	while(i < n)
	{
		max = 0;
		sal = a[i];
		for(j = i+1 ; j<i+sal ; j++)
		{
			if(a[j] == 0)
			{
				c=0;
				printf("Not possible");
				break;
			}
			elseif(a[j]>max) 
			{
				max = a[j];
				t = j;
			}
		}
		i = t;
		c++;
	}
	if(c != 0 )
	{
		printf("%d",c);
	}
}	  