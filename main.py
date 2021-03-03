import requests
from bs4 import BeautifulSoup


url = "https://forum.dataak.com/index.php"

payload = "<file contents here>"
headers = {
  'Cookie': 'loginattempts=1; sid=7072d51c3db1cb252e4f83e42995ab97; mybb[lastvisit]=1614768916; mybb[lastactive]=1614770008; mybbuser=2_b9uUv4HxuJEqmUp5XDzVmvVdpwBTBMUmw7cAscxZJOQwSbk4Sm',
  'Content-Type': 'text/plain'
}

resp = requests.request("GET", url, headers=headers, data = payload, verify=False,)
soup = BeautifulSoup(resp.text)
s=soup.find_all('div',{"id":"container"})
category = ''
dictcategory={}
dictcrawl={}
datacrawllist=[]
dictdatacrawl={}
import time
o=0
for i in s[0].find_all('table',{"class":"tborder"}):
  listdata=[]
  dictcrawl={}
  for x in i.find_all('tr'):
    if len(i.find_all('td',{"class":"thead"})[0].find_all('a'))!=0:
      category = i.find_all('td',{"class":"thead"})[0].find_all('a')[0].text
    if len(x.find_all('td', {"class": "tcat"})) == 0:
      if len(x.find_all('td', {"class": "thead"})) == 0:
        if len(x.text)>1:
          countCategory=''
          countSend=''
          community=''
          for item in x.find_all('td'):
            if len(x.find_all('strong'))!= 0:
              community = x.find_all('strong')[0].find_all('a')[0].text.rstrip().lstrip()
            if  len(item.find_all('strong'))==0:
              if  len(item.find_all('span'))==0:
                if  len(item.find_all('div'))==0:
                  if countCategory =='':
                    countCategory=item.text.rstrip().lstrip()
                  else:
                    countSend=item.text.rstrip().lstrip()
          if len(community)!=0:
            dictcategory={"community":community,"countCategory":countCategory,"countSend":countSend}
            if  len(dictcategory)!=0:
              listdata.append(dictcategory)
              
  if len(listdata)!=0:
    dictcrawl[category]=listdata
    datacrawllist.append(dictcrawl)
  
  
  
  
  
dictdatacrawl['crawlfromdataak']=datacrawllist
print(datacrawllist)
# for item in dictdatacrawl['crawlfromdataak']:
#   # for key in item.keys():
#   print(item)




