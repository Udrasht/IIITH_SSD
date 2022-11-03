import csv
from functools import reduce
globlist=[]
with open('lab_11_data.csv', mode ='r')as file:
	csvFilepointer = csv.reader(file)
	for lines in csvFilepointer:
		globlist.append(lines[0:7])
#print(globlist)
# second question

result = list(filter(lambda x: (float(x[6])>-3.0 ), globlist[1:]))
result.insert(0,globlist[0]);
#print(result)
#third Question
a=[]
for i in range(1,len(result)):
	p=result[i][1].replace(",","")
	a.append(float(p))
sum23=reduce(lambda d,c:d+c,a)	
#print(sum23/len(result))
a1=[]
for i in range(1,len(result)):
	p1=result[i][2].replace(",","")
	a1.append(float(p1))
sum24=reduce(lambda d,c:d+c,a1)	
#print(sum24/len(result))
a2=[]
for i in range(1,len(result)):
	p1=result[i][3].replace(",","")
	a2.append(float(p1))
sum25=reduce(lambda d,c:d+c,a2)	
#print(sum25/len(result))
str1=str(sum23/len(result))+"\n"+str(sum24/len(result))+"\n"+str(sum25/len(result))
#print(str1)
file1 = open('avg_output.txt', 'w')  
file1.write(str1)
file1.close()
#fourth question
reslist=[];
inp=input("Enter character: ")
reslist.append(result[0])
for j in result:
	if(j[0][0]==inp):
		reslist.append(j)

		
		
print(reslist)
file2 = open('stock_output.txt', 'w+', newline ='')
for k in reslist:
	udpal=' '.join([str(elem) for elem in k ])
	udpal+='\n'
	file2.write(udpal)
	



	
 
