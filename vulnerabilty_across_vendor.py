total=[]
file=open('vendor_data.txt')
lines=file.readlines()
file.close()
total_count=0
for i in lines:
    arr=i.split(" ")
    total.append(int(arr[1]))
    total_count+=int(arr[1])
import matplotlib.pyplot as plt
partial_sum=0
percentages=[]
vendor_count=[]
it=0
for i in total:
    it+=1
    partial_sum+=i
    percent=partial_sum*100.0/total_count
    percentages.append(percent)
    vendor_count.append(it)
plt.plot(vendor_count,percentages)
plt.ylabel('Percentage of Vulnerabilites')
plt.xlabel('Vendor Count')
plt.title('Distrubution of Vulnerabilites Across All Vendors (2014–2024)')
plt.yticks(range(0, 110, 10))
plt.legend()
plt.tight_layout()
plt.show()