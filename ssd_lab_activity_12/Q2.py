from datetime import datetime
file1 = open('input.txt', 'r')
Lines = file1.readlines()
count = 0
footcount = []
footmat = 0
count = 0
re = 0
p = 0
farr = []
tarr = []
te = ""
ccout=0
for line in Lines:
    count += 1
    if (len(line.strip()) == 0 and ccout==126):

        if (len(footcount) != 0):
            po = 0
            for i in range(0, 125):
                for j in range(1, 25):
                    if (int(footcount[i][j]) != 0 and int(footcount[i][j+1]) != 0 and int(footcount[i+1][j]) != 0):
                        if (re == 0 and p == 0):
                            re = i
                            te=footcount[62][0]
                            p = 1
                        elif (abs(i-re) > 3 and i != re):
                            farr.append(re)
                            tarr.append(te)
                            te=footcount[62][0]
                            re = i
                        else:
                            re = i
                            te=footcount[62][0]
                            po = 1
                if (po == 1):
                    break
            #print(int(footcount[2][3])+int(footcount[3][2]))
            footcount = []
            ccout=0
    else:
    	if(len(line.strip()) != 0):
    		searchlist1 = line.split("\t")
    		footcount.append(searchlist1)
    		ccout+=1
    		
        
        #print(line.strip())



#print(count)
po = 0
for i in range(0, 125):
    for j in range(1, 25):
        if (int(footcount[i][j]) != 0 and int(footcount[i][j+1]) != 0 and int(footcount[i+1][j]) != 0):
            if (re == 0 and p == 0):
                re = i
                te=footcount[62][0]
                p = 1

            elif (i+1 != re and i != re):
                farr.append(re)
                tarr.append(te)
                te=footcount[62][0]
                

                re = i

            else:
                #print(i)
                te=footcount[62][0]
                re = i

            po = 1
    if (po == 1):
        break

farr.append(re)
tarr.append(te)
#print(tarr)
#print(te)
file1.close()
#print(len(footcount))
#print(farr)
durat=0;
tyt=0;
leg="Left"
lft=0
rft=0
piu=0
for i in range(len(tarr)-2):
	if(tyt%2==0):
		leg="Left"
		lft+=1;
		piu=lft
	else:
		leg="Right"
		rft+=1
		piu=rft
		
	x=tarr[i]
	y=tarr[i+2]
	start_time = datetime.strptime(x[0:8], "%H:%M:%S")
	end_time = datetime.strptime(y[0:8], "%H:%M:%S")
	yu=end_time-start_time
	sec = yu.total_seconds()
	durat=int(sec)
	distance=abs(int(farr[i+2])-int(farr[i]))
	print("Stride Length of ",piu," step of ",leg," foot: ",distance,"cm")
	vel=distance/int(sec)
	print("Stride Velocity: ",vel,"cm/sec")
	cad=(60/sec)*3
	print("Cadence(Number of steps per minute) : ",round(cad))
	tyt+=1
        #print("Stride Velocity: ",vel)
        
        
	

