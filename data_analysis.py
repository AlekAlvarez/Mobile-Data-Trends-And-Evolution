cwe_dictionary_file=open('699.csv')
cwe_dictionary={}
cwe_dictionary_file=cwe_dictionary_file.readlines()
for i in range(len(cwe_dictionary_file)):
    if i!=0:
        ls=cwe_dictionary_file[i].split(",")
        cwe_dictionary[ls[0]]=" ".join(cwe_dictionary_file[len(ls[0]):])
import json, csv,re
totalVulnerabiltyString="Year,Mobile Vulnerablities,Total Vulnerabities"
for i in range(6,17):
    num=str(i)
    if len(num)==1:
        num="0"+num
    fileName="nvdcve-1.1-20"+num+".json"
    file=open(fileName,'r')
    data=json.load(file)
    data=data['CVE_Items']
    mobile_data=open("mobile_data_"+num+".txt",'w')
    totalVulnerablities=0
    possibleMobile=0
    #print(data[3]['cve'])'
    for i in data:
        #KEYS: 'cve', 'configurations', 'impact', 'publishedDate', 'lastModifiedDate'
        #cve Keys 'data_type', 'data_format', 'data_version', 'CVE_data_meta', 'problemtype', 'references', 'description'
        #problemtype keys 'problemtype_data' which leads to 'description' which leads to 'value' which has CWE info
        #description Key 'description_data' (is a list with one value a JSON) to access the value use 'value'
        CVE_ID=i['cve']['CVE_data_meta']['ID']
        CVSS_data=i['impact']
        CWE_id=""
        contains_cwe_id=False
        totalVulnerablities+=1
        if 'problemtype' in i['cve'].keys() and 'problemtype_data' in i['cve']['problemtype'] and len(i['cve']['problemtype']['problemtype_data'])>0 and len(i['cve']['problemtype']['problemtype_data'][0]['description'])>0:
            CWE_id=i['cve']['problemtype']['problemtype_data'][0]['description'][0]['value']
            contains_cwe_id=True
        summary=i['cve']['description']['description_data'][0]['value']
        #re.search("\sios\s",description)  or
        b=False
        if contains_cwe_id and CWE_id[4:] in cwe_dictionary:
            val=cwe_dictionary[CWE_id[4:]].lower()
            if "mobile" in val or "android" in val:
                b=True
        if b or 'mobile' in summary or 'android' in summary or 'watchos' in summary or 'iphone' in summary or re.search(r".*\sios.*",summary)!=None:
            mobile_data.write(CVE_ID+'\n')
            mobile_data.write(summary+"\n")
            if contains_cwe_id:
                mobile_data.write(CWE_id+'\n')
            mobile_data.write("\n\n")
            possibleMobile+=1
    mobile_data.close()
    file.close()
    print(possibleMobile)
    print(totalVulnerablities)
    totalVulnerabiltyString+="\n"+num+","+str(possibleMobile)+","+str(totalVulnerablities)
total_data=open("total_data.txt","w")
total_data.write(totalVulnerabiltyString)
total_data.close()
