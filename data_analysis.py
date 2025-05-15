import json, csv,re
file=open("nvdcve-1.1-2017.json",'r')
data=json.load(file)
data=data['CVE_Items']
mobile_data=open("mobile_data.txt",'w')
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
    if 'problemtype' in i['cve'].keys() and 'problemtype_data' in i['cve']['problemtype'] and len(i['cve']['problemtype']['problemtype_data'])>0 and len(i['cve']['problemtype']['problemtype_data'][0]['description'])>0:
        CWE_id=i['cve']['problemtype']['problemtype_data'][0]['description'][0]['value']
        contains_cwe_id=True
    summary=i['cve']['description']['description_data'][0]['value']
    #re.search("\sios\s",description)  or
    if 'mobile' in summary or 'android' in summary or 'watchos' in summary or 'iphone' in summary or re.search(r".*\sios.*",summary)!=None:
        mobile_data.write(CVE_ID+'\n')
        mobile_data.write(summary+"\n")
        if contains_cwe_id:
            mobile_data.write(CWE_id+'\n')
        mobile_data.write("\n\n")
        possibleMobile+=1
mobile_data.close()
file.close()
print(possibleMobile)