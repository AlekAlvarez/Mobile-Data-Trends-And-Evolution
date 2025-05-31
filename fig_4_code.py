import matplotlib.pyplot as plt
total=[]
for i in range(14, 25):
    file=open("mobile_data_"+str(i)+".txt")
    lines=file.readlines()
    local=0
    adj=0
    net=0
    for j in range(len(lines)):
        if 'ADJACENT_NETWORK' in lines[j] and len(lines[j])<=20:
            adj+=1
        elif 'LOCAL' in lines[j] and len(lines[j])<=20:
            local+=1
        elif 'NETWORK' in lines[j] and len(lines[j])<=20:
            net+=1
    dictionary={}
    dictionary['ADJACENT_NETWORK']=adj
    dictionary['LOCAL']=local
    dictionary['NETWORK']=net
    total.append(dictionary)
local_vals = [year_data['LOCAL'] for year_data in total]
network_vals = [year_data['NETWORK'] for year_data in total]
adjacent_vals = [year_data['ADJACENT_NETWORK'] for year_data in total]
total_counts = [local_vals[i] + network_vals[i] + adjacent_vals[i] for i in range(len(local_vals))]
local_pct = [100 * local_vals[i] / total_counts[i] if total_counts[i] > 0 else 0 for i in range(len(local_vals))]
network_pct = [100 * network_vals[i] / total_counts[i] if total_counts[i] > 0 else 0 for i in range(len(local_vals))]
adjacent_pct = [100 * adjacent_vals[i] / total_counts[i] if total_counts[i] > 0 else 0 for i in range(len(local_vals))]
years=[2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024]
bar_width = 0.5
plt.figure(figsize=(10, 6))
plt.bar(years, local_pct, color='black', label='Local')
plt.bar(years, network_pct, bottom=local_pct, color='lightgray', label='Network')
bottoms = [local_pct[i] + network_pct[i] for i in range(len(years))]
plt.bar(years, adjacent_pct, bottom=bottoms, color='gray', label='Adjacent')

plt.ylabel('Percentage')
plt.xlabel('Year')
plt.title('Mobile Data Type Distribution (2007–2016)')
plt.xticks(years)
plt.yticks(range(0, 110, 10))
plt.legend()
plt.tight_layout()
plt.show()