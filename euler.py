import math
l =[]
newcount = 0
for i in range(2,14063 , 2):
	count = 0
	if i%2 == 0 and i%3 == 0 and i!=6: #because every number which is divisible
		newcount += 1 #  by 2 and 3 both will definately be an abundant number 
		l.append(i)#because divide by 2 means it has half of that number in its 
	else: #divisor and divide by 3 means it has 1/3rd the number in its divisor 
		n = math.ceil(math.sqrt(i))#, and then 1 , 2,3 will also be counted. and 
		total = 1 #any number which again be divided by 2 or 3 so its divisor sum 
		divisor =2#will definitely be greater than 2.
		while (divisor < n):
			if (i%divisor == 0):
				total += divisor
				total += i//divisor
			divisor+=1
		if n**2==i:
			total+=n
		if total > i:
			l.append(i)
m=[]
for i in range(len(l)):
	for j in range(len(l)):
		m.append(l[i] + l[j])
l = list(range(1,28124))
l = set(l)
m = set(m)
print(sum(l-m))