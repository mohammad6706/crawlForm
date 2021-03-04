import main
import dbdata

db=dbdata.dbmysql()
datadict=main.getCrawl()

for item in datadict:
    catidstr = ''
    community=''
    countCategory=''
    countSend=''
    for key in item.keys():
        catid=db.serchtbl_cat(key)
        if  len(catid) == 0:
            if db.inserttbl_category(key):
                catidstr=db.serchtbl_cat(key)[0][0]
        else:
            catidstr=catid[0][0]
    for x in item:
        for record in item[x]:
            community = record['community']
            countCategory = record['countCategory']
            countSend = record['countSend']
            import time
            if db.serchtbl_detail(community):
                if db.inserttbl_detail(catidstr,community,countCategory,countSend):
                    print('record Successful')
                    time.sleep(5)
            else:
                print('record Unsuccessful')
                time.sleep(5)

print(db.showdatacrawl())
