import matplotlib.pyplot as plt
total=[]
for i in range(14, 25):
    file=open("mobile_data_"+str(i)+".txt")
    lines=file.readlines()
    low=0
    medium=0
    high=0
    for j in range(len(lines)):
        if 'Complexity' in lines[j]:
            if "LOW" in lines[j]:
                low+=1
            elif "MEDIUM" in lines[j]:
                medium+=1
            elif "HIGH" in lines[j]:
                high+=1
    dictionary={}
    print(high)
    dictionary["LOW"]=low
    dictionary['MEDIUM']=medium
    dictionary["HIGH"]=high
    total.append(dictionary)
low_vals = [year_data['LOW'] for year_data in total]
medium_vals = [year_data['MEDIUM'] for year_data in total]
high_vals = [year_data['HIGH'] for year_data in total]
total_counts = [low_vals[i] + medium_vals[i] + high_vals[i] for i in range(len(low_vals))]
low_pct = [100 * low_vals[i] / total_counts[i] if total_counts[i] > 0 else 0 for i in range(len(low_vals))]
medium_pct = [100 * medium_vals[i] / total_counts[i] if total_counts[i] > 0 else 0 for i in range(len(low_vals))]
high_pct = [100 * high_vals[i] / total_counts[i] if total_counts[i] > 0 else 0 for i in range(len(low_vals))]
years=[2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024]
bar_width = 0.5
plt.figure(figsize=(10, 6))
plt.bar(years, low_pct, color='black', label='Low')
plt.bar(years, medium_pct, bottom=low_pct, color='lightgray', label='Medium')
bottoms = [low_pct[i] + medium_pct[i] for i in range(len(years))]
plt.bar(years, high_pct, bottom=bottoms, color='gray', label='High')

plt.ylabel('Percentage')
plt.xlabel('Year')
plt.title('Access Complexity (2007–2016)')
plt.xticks(years)
plt.yticks(range(0, 110, 10))
plt.legend()
plt.tight_layout()
plt.show()