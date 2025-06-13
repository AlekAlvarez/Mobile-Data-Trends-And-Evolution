totalCWE={}
file=open("1000.csv")
lines=file.readlines()
file.close()
for i in range(len(lines)):
    if i !=0:
        line=lines[i].split(',')
        Error_id=int(line[0])
        if Error_id not in totalCWE.keys():
            totalCWE[Error_id]=line[1]
file=open("1194.csv")
lines=file.readlines()
file.close()
for i in range(len(lines)):
    if i !=0:
        line=lines[i].split(',')
        Error_id=int(line[0])
        if Error_id not in totalCWE.keys():
            totalCWE[Error_id]=line[1]
file=open("699.csv")
lines=file.readlines()
file.close()
for i in range(len(lines)):
    if i !=0:
        line=lines[i].split(',')
        Error_id=int(line[0])
        if Error_id not in totalCWE.keys():
            totalCWE[Error_id]=line[1]
import matplotlib.pyplot as plt
total={}
for i in range(14, 25):
    print(i)
    file=open("mobile_data_"+str(i)+".txt")
    lines=file.readlines()
    file.close()
    for j in lines:
        if "CWE-" ==j[0:4] and len(j)<=8:
            id=j[4:]
            id=int(id)
            if id in total.keys():
                total[id]+=1
            else:
                total[id]=1
sorted_data = dict(sorted(total.items(), key=lambda item: item[1], reverse=True))
total_count=0
file=open("ranked_cwe.txt",'w')
count=0
names=[]
for i in sorted_data.keys():
    total_count+=total[i]
    if count<11:
        names.append(totalCWE[i])
    count+=1
    if i in totalCWE:
        file.write(totalCWE[i]+" ")
    file.write("Error: "+str(i)+" frequency: "+str(total[i])+'\n')
print(total_count)
print(names)
count=0
partial_sum=0
percantages=[]
counts=[]
names=["Exposure of Sensitive Information","Race Condition","Hard Coded Credentials","Improper Certificate Validation"
       ,"Cleartext Transmission of Sensitive Information","Cleartext Storage of Sensitive information","Missing Release of Resource after Effective Lifetime",
       "Imporoper Memory Buffer Restrictions","Improper Input Validation","Out of bounds Write","Out of bounds Read"]
for i in sorted_data.keys():
    if count==11:
        break
    count+=1
    counts.append(sorted_data[i])
    partial_sum+=sorted_data[i]
    percantages.append(partial_sum/total_count*100)
fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.bar(names, counts, color='grey')
ax1.set_ylabel("CVE Count", color='black')
ax1.set_xlabel("Vulnerability Type")
ax1.tick_params(axis='y', labelcolor='black')
ax1.tick_params(axis='x', rotation=45)
labels = plt.xticks(rotation=45)[1]
for label in labels:
    label.set_ha('right')
plt.subplots_adjust(bottom=0.25) 
ax2 = ax1.twinx()
ax2.plot(names, percantages, color='black', marker='o')
ax2.set_ylabel("Cumulative %", color='black')
ax2.tick_params(axis='y', labelcolor='black')
ax2.set_ylim(0, 110)
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()