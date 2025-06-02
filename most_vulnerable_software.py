data=open("most_vulnerable_software_data.txt",'w')
total={}
for i in range(14,25):
    file=open("mobile_data_"+str(i)+".txt")
    lines=file.readlines()
    file.close()
    for j in range(len(lines)):
        if "CPE 23 Uri:" in lines[j]:
            arr=lines[j].split(":")
            if len(arr)>5:
                venodor=arr[4]
                venodor=venodor.lower()
                affected_software=venodor+" "+(arr[5]).lower()
                if affected_software in total.keys():
                    total[affected_software]+=1
                else:
                    total[affected_software]=1
sorted_data = dict(sorted(total.items(), key=lambda item: item[1], reverse=True))
total=sorted_data
for i in total.keys():
    data.write(i+" "+str(total[i])+'\n')
data.close()