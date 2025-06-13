file=open("vendor_data.txt")
lines=file.readlines()
file.close()
total=0
for i in lines:
    num=i.split(" ")[1]
    num=int(num)
    total+=num
partial_sum=0
for i in range(len(lines)):
    num=lines[i].split(" ")[1]
    num=int(num)
    partial_sum+=num
    if partial_sum>=total/2:
        print(i)
        break
    