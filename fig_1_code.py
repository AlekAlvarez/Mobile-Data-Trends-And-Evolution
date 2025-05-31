import matplotlib.pyplot as plt
file=open("total_data.txt","r")
lines=file.readlines()
file.close()
years=[]
mobiles=[]
non_mobiles=[]
for i in range(1,len(lines)):
    strings=lines[i].split(',')
    year=int(strings[0])
    mobile_vulnerabilities=int(strings[1])
    total_vulnerabilities=int(strings[2])
    non_mobile=total_vulnerabilities-mobile_vulnerabilities
    years.append(year)
    mobiles.append(mobile_vulnerabilities)
    non_mobiles.append(non_mobile)
plt.plot(years,mobiles,color='black',linestyle='-',label="Mobile")
plt.plot(years,non_mobiles,color='grey',linestyle='--',label="Non-Mobile")
plt.xticks(years,["2014","2015","2016","2017","2018","2019","2020","2021","2022","2023","2024"])
plt.legend()
plt.show()