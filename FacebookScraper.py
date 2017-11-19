import re

r = re.compile('alt="" aria-label="(.*?)" role="img" /></a>')

temp = []
#with open('OverheardAtRpi.txt', "r", encoding="utf-8") as f:
    
    
with open('OverheardAtRpi.txt', "r", encoding="utf-8") as f:
    for i in f.readlines():
        print(i)
        if(r.findall(i)):
            m = r.findall(i)
            temp.append(m)
nameList = []
for eachList in temp:
    for names in eachList:
        nameList.append(names)
        
print(nameList)
print(len(nameList))
