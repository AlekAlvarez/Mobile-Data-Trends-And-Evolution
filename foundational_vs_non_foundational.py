import matplotlib.pyplot as plt
total_driod=0
found_driod=0
non_driod=0
total_ios=0
found_ios=0
non_ios=0
for i in range(14, 25):
    file=open("mobile_data_"+str(i)+".txt")
    lines=file.readlines()
    file.close()
    for j in range(len(lines)):
        if "CPE 23 Uri:" in lines[j]:
            arr=lines[j].split(":")
            if len(arr)>5:
                venodor=arr[4]
                venodor=venodor.lower()
                software=(arr[5]).lower()
                ios=False
                andriod=False
                if venodor=="apple" or software=="ios":
                    ios=True
                if not ios and (venodor == "google" or software=="android"):
                    andriod=True
                if not andriod and not ios:
                    continue
                info=lines[j+1]
                isFound=False
                if "foundational" in info:
                    isFound=True
                if ios:
                    total_ios+=1
                    if isFound:
                        found_ios+=1
                    else:
                        non_ios+=1
                if andriod:
                    total_driod+=1
                    if isFound:
                        found_driod+=1
                    else:
                        non_driod+=1
print(str(total_ios)+" "+str(found_ios)+" "+str(non_ios))
print(str(total_driod)+" "+str(found_driod)+" "+str(non_driod))
labels = ['iOS', 'Android']
foundational = [found_ios/total_ios*100, found_driod/total_driod*100]
non_foundational = [non_ios/total_ios*100, non_driod/total_driod*100]
x = range(len(labels))
fig, ax = plt.subplots()
bar1 = ax.bar(x, foundational, label='Foundational', color='black')
bar2 = ax.bar(x, non_foundational, bottom=foundational, label='Non-Foundational',  color='white', edgecolor='black')
for i in range(len(labels)):
    ax.text(x[i], foundational[i] / 2, f'{foundational[i]:.2f}%', ha='center', va='center', color='white', fontsize=10)
    ax.text(x[i], foundational[i] + non_foundational[i] / 2, f'{non_foundational[i]:.2f}%', ha='center', va='center', color='black', fontsize=10)
ax.set_ylabel('Total Vulnerabilities')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_yticks(range(0, 110, 10))
ax.set_ylim(0, 100)
ax.legend()
plt.tight_layout()
plt.show()