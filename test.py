from bs4 import BeautifulSoup as bs
import json
sp=bs(open('test.html', encoding='utf-8'), 'html.parser')
tar=sp.find_all('div', {'class':'term'})
l=[]
# for i in tar[:1]:
    
#     for j in i.find_all('p'):
#         print(str(j).replace('\n', '').replace('  ', ''))
    
    

p={'t':5, 'd':4}
print(json.dumps(p))
# for i in tar[:1]:
#     t=i.find('h2').text.strip()
#     d=''
#     for j in i.find_all('p'):
#         d+=str(j).replace('\n', '').replace('  ', '')
    
#     l.append()

#     with open('giuded.js', 'w') as ff:
#         print(l, file=ff)