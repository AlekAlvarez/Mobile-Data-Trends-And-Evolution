cwe_dictionary_file=open('919.csv')
cwe_dictionary={}
cwe_dictionary_file=cwe_dictionary_file.readlines()
for i in range(len(cwe_dictionary_file)):
    if i!=0:
        ls=cwe_dictionary_file[i].split(",")
        cwe_dictionary[ls[0]]=" ".join(cwe_dictionary_file[len(ls[0]):])
import json, csv,re
totalVulnerabiltyString="Year,Mobile Vulnerablities,Total Vulnerabities"
for i in range(14,25):
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
        affected_software = ""
        config=i['configurations']
        nodes=config['nodes']
        cpe23URI=''
        containsRange=False
        publishedDate=i["publishedDate"]
        for stuff in nodes:
            if "cpe_match" in stuff.keys():
                cpe_match=stuff['cpe_match']
                for more_stuff in cpe_match:
                    if "cpe23Uri" in more_stuff.keys():
                        cpe23URI=more_stuff["cpe23Uri"]
        accessVector=''
        severity=''
        complexity=''
        containsAccess=False
        containsSeverity=False
        containsComplexity=False
        foundational=False
        if "baseMetricV3" in CVSS_data.keys():
            accessVector=CVSS_data["baseMetricV3"]["cvssV3"]["attackVector"]
            severity=CVSS_data["baseMetricV3"]["cvssV3"]["baseSeverity"]
            complexity=CVSS_data["baseMetricV3"]["cvssV3"]["attackComplexity"]
            containsAccess=True
            containsSeverity=True
            containsComplexity=True
        elif "baseMetricV2" in CVSS_data.keys():
            accessVector=CVSS_data["baseMetricV2"]["cvssV2"]["accessVector"]
            severity=CVSS_data["baseMetricV2"]["severity"]
            complexity=CVSS_data["baseMetricV2"]["cvssV2"]["accessComplexity"]
            containsAccess=True
            containsSeverity=True
            containsComplexity=True
        CWE_id=""
        contains_cwe_id=False
        totalVulnerablities+=1
        if 'problemtype' in i['cve'].keys() and 'problemtype_data' in i['cve']['problemtype'] and len(i['cve']['problemtype']['problemtype_data'])>0 and len(i['cve']['problemtype']['problemtype_data'][0]['description'])>0:
            CWE_id=i['cve']['problemtype']['problemtype_data'][0]['description'][0]['value']
            contains_cwe_id=True
        summary=i['cve']['description']['description_data'][0]['value']
        arr=cpe23URI.split(":")
        if "version 1.0" in summary.lower() or "all versions" in summary or len(arr)>5 and "1.0" == arr[5]:
            foundational=True
        #re.search("\sios\s",description)  or
        b=False
        if contains_cwe_id and CWE_id[4:] in cwe_dictionary:
            val=cwe_dictionary[CWE_id[4:]].lower()
            b=True
        if b or 'mobile' in summary or 'android' in summary or 'watchos' in summary or 'iphone' in summary or re.search(r".*\sios.*",summary)!=None and not "Cisco IOS" in summary:
            mobile_data.write(CVE_ID+'\n')
            mobile_data.write(summary+"\n")
            if contains_cwe_id:
                mobile_data.write(CWE_id+'\n')
            if containsAccess:
                mobile_data.write(accessVector+'\n')
                mobile_data.write("Severity: "+severity+'\n')
                mobile_data.write("Complexity: "+complexity+'\n')
            mobile_data.write("CPE 23 Uri: "+cpe23URI+'\n')
            if foundational:
                mobile_data.write("foundational")
            else:
                mobile_data.write("Not Foundational")
            mobile_data.write("\nPublished Date: "+publishedDate)
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
