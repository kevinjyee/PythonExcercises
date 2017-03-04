def main():
	i =0; 
	j =0;
	sum1 =0;
	sum2 =0;
	for i in range(0,10000):
	
		sum1 += i;
		sum2 =0;
		for j in range(i+2,sum1+1):
			sum2+= j;
			
			if(sum1 == sum2):
				print (i)

	


main()