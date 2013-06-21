import re
import collections as col

ext=col.Counter()
dirtree=open('ls.log.txt','r')
count=0
for line in dirtree.readlines():
    matchDirname=re.match(r'^www2.census.gov',line)
    if matchDirname:
        dir = line.rstrip()
    else:
        items=re.split(r'\s*',line);
        if len(items)>4 and int(items[4])>200:
            size=int(items[4])
            #print dir,'\t'.join(items[4:])
            name=items[8].split('.')
            if len(name)>1:
                lname=name[-1].lower()
                ext[lname] += size
            count +=1
            if count % 10000 == 0:
                print count

dirtree.close()
Sext=sorted(ext.items(),key=lambda item: item[1],reverse=True)
Sum=sum([item[1] for item in Sext])

print [(item, (item[1]+0.0)/Sum) for item in Sext]

BigExt=['zip','dbf','gz','dat','xls','csv','txt']

print '============================================'

dirtree=open('ls.log.txt','r')
for line in dirtree.readlines():
    matchDirname=re.match(r'^www2.census.gov',line)
    if matchDirname:
        dir = line.rstrip()
    else:
        items=re.split(r'\s*',line);
        if len(items)>4 and int(items[4])>200:
            size=int(items[4])
            name=items[8].split('.')
            if len(name)>1:
                lname=name[-1].lower()
                if lname in BigExt:
                    print dir,' '.join(items[4:])
                    #count +=1
                    #if count >1000:
                    #    break




