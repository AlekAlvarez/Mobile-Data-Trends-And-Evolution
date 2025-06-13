file=open("most_vulnerable_software_data.txt")
lines=file.readlines()
file.close()
data=open('vendor_data.txt','w')
total={}
for i in lines:
    vend=i.split(" ")[0]
    if vend in total.keys():
        total[vend]+=1
    else:
        total[vend]=1
sorted_data = dict(sorted(total.items(), key=lambda item: item[1], reverse=True))
total=sorted_data
for i in total.keys():
    data.write(i+" "+str(total[i])+'\n')
data.close()