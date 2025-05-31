import matplotlib.pyplot as plt
appCWES=[]
osCWES=[]
file=open("699.csv")
lines=file.readlines()
file.close()
for i in range(1,len(lines)):
    num=lines[i].split(",")[0]
    appCWES.append(int(num))
file=open("1194.csv")
lines=file.readlines()
file.close()
for i in range(1,len(lines)):
    num=lines[i].split(",")[0]
    osCWES.append(int(num))
yearData=[]
for i in range(14, 25):
    file=open("mobile_data_"+str(i)+".txt")
    lines=file.readlines()
    app=0
    both=0
    os=0
    for j in range(len(lines)):
       if "CWE" in lines[j] and len(lines[j])<10:
           print(id)
           id=int(lines[j][4:]) 
           if id in osCWES and id in appCWES:
               both+=1
           elif id in osCWES:
               os+=1
           elif id in appCWES:
               app+=1
    dictionary={}
    dictionary["both"]=both
    dictionary["os"]=os
    dictionary["app"]=app    
    file.close()
    yearData.append(dictionary)
print(yearData)
