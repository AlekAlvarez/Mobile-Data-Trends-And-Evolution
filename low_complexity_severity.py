import matplotlib.pyplot as plt
total=[]
data=open("CaseStudy.txt",'w')
for i in range(14, 25):
    data.write(str(i)+"\n")
    file=open("mobile_data_"+str(i)+".txt")
    lines=file.readlines()
    low=0
    medium=0
    high=0
    track=0
    for j in range(len(lines)):
        if 'Severity' in lines[j]:
            if "HIGH" in lines[j] and "LOW" in lines[j+1]:
                track+=1
                data.write(lines[j-4])
                data.write(lines[j-3])
                data.write(lines[j-2])
                data.write(lines[j-1])
                data.write(lines[j])
                data.write(lines[j+1])
                data.write(lines[j+2])
                data.write(lines[j+3])
                data.write(lines[j+4])
                data.write('\n')
    total.append(track)
    print(track)
years=[2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024]
bar_width = 0.5
plt.figure(figsize=(10, 6))
plt.bar(years, total, color='red')

plt.ylabel('Vunerability Count')
plt.xlabel('Year')
plt.title('Vulnerabilties with low complexity and high severity (2014–2024)')
plt.xticks(years)
#plt.yticks(range(0, , 10))
plt.legend()
plt.tight_layout()
plt.show()