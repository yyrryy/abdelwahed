import requests as req
from bs4 import BeautifulSoup as bs
from random import choice


def tr(word):
    
    base='https://showmeword.com'
    url='https://showmeword.com/definition/english_word/'





    uag=['Mozilla/5.0 (X11; CrOS x86_64 13982.88.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.162 Safari/537.36', 'Mozilla/5.0 (X11; CrOS x86_64 13597.94.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.186 Safari/537.36', 'Mozilla/5.0 (X11; CrOS x86_64 13597.105.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.208 Safari/537.36', 'Mozilla/5.0 (X11; CrOS x86_64 13904.97.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.167 Safari/537.36', 'Mozilla/5.0 (X11; CrOS x86_64 14092.66.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.95 Safari/537.36', 'Mozilla/5.0 (X11; CrOS x86_64 13729.56.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.95 Safari/537.36']
    h={
    'user-agent': choice(uag)
    }
    with req.Session() as session:

        h={
        'user-agent': choice(uag)
        }
        data=session.get('https://showmeword.com/definition/english_word/'+word, headers=h).content.decode('utf-8')
        sp=bs(data, 'html.parser')
        ad=sp.find('audio', {'id':'audio_uk'}).find('source')['src']
        h={
        'user-agent': choice(uag)
        }
        mp=base+ad
        
        tar=[i.text.strip() for i in sp.find_all('span', {'class':'transcription'})]
        if tar:
            br=  tar[1]
        

        print(br)
        return mp, br
        


