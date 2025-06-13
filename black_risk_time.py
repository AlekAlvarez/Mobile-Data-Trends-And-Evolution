import matplotlib.pyplot as plt
data=open("black_risk_data.txt","w")
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
                andriod=False
                if (venodor == "google" or software=="android"):
                    andriod=True
                info=lines[j+1]
                isFound=False
                if "foundational" in info:
                    isFound=True
                if andriod:
                    if isFound:
                        date=lines[j+2]
                        date=date.split(" ")[2]
                        date=date.split('-')
                        date="\\".join(date)
                        date=date[0:10]
                        data.write(software+" "+date+"\n")
data.close()