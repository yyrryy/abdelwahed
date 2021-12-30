import requests as req
from bs4 import BeautifulSoup as bs
from random import choice

def tr(word):
    
    base='https://showmeword.com'





    uag=['Mozilla/5.0 (X11; CrOS x86_64 13982.88.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.162 Safari/537.36', 'Mozilla/5.0 (X11; CrOS x86_64 13597.94.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.186 Safari/537.36', 'Mozilla/5.0 (X11; CrOS x86_64 13597.105.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.208 Safari/537.36', 'Mozilla/5.0 (X11; CrOS x86_64 13904.97.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.167 Safari/537.36', 'Mozilla/5.0 (X11; CrOS x86_64 14092.66.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.95 Safari/537.36', 'Mozilla/5.0 (X11; CrOS x86_64 13729.56.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.95 Safari/537.36']
    h={
    'user-agent': choice(uag)
    }

    h={
    'user-agent': choice(uag)
    }
    data=req.get('https://showmeword.com/definition/english_word/'+word, headers=h).content.decode('utf-8')
    sp=bs(data, 'html.parser')
    ad=sp.find('audio', {'id':'audio_uk'}).find('source')['src']
    h={
    'user-agent': choice(uag)
    }
    mp=base+ad
    
    tar=[i.text.strip() for i in sp.find_all('span', {'class':'transcription'})]
    if tar:
        br=  tar[1]
    

    return mp, br
        

def strss(w):
     

    uag=['Mozilla/5.0 (X11; CrOS x86_64 13982.88.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.162 Safari/537.36', 'Mozilla/5.0 (X11; CrOS x86_64 13597.94.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.186 Safari/537.36', 'Mozilla/5.0 (X11; CrOS x86_64 13597.105.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.208 Safari/537.36', 'Mozilla/5.0 (X11; CrOS x86_64 13904.97.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.167 Safari/537.36', 'Mozilla/5.0 (X11; CrOS x86_64 14092.66.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.95 Safari/537.36', 'Mozilla/5.0 (X11; CrOS x86_64 13729.56.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.95 Safari/537.36']
    h={
    'user-agent': choice(uag)
    }

    data=req.get('https://www.howmanysyllables.com/words/'+w, headers=h).content.decode('utf-8')
    sp=bs(data, 'html.parser')
    root=sp.find('div', {'id':'Syllables'})
    syll=root.find_all('span', {'class':'Answer_Red'})[1].text
    press=root.find('span', {'class':'no_b'})
    nsyll=len(syll.split('-'))
    return nsyll, press
    

    
def verb(v):
    url="https://www.theconjugator.com/english/verb/to+{}.html"
    uag=['Mozilla/5.0 (X11; CrOS x86_64 13982.88.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.162 Safari/537.36', 'Mozilla/5.0 (X11; CrOS x86_64 13597.94.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.186 Safari/537.36', 'Mozilla/5.0 (X11; CrOS x86_64 13597.105.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.208 Safari/537.36', 'Mozilla/5.0 (X11; CrOS x86_64 13904.97.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.167 Safari/537.36', 'Mozilla/5.0 (X11; CrOS x86_64 14092.66.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.95 Safari/537.36', 'Mozilla/5.0 (X11; CrOS x86_64 13729.56.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.95 Safari/537.36']
    h={
    'user-agent': choice(uag)
    }

    data=req.get(url.format(v), headers=h).content.decode('utf-8')
    sp=bs(data, 'html.parser')
    root=sp.find('div', {'class':'verbe'}).find('p').text
    return root

def paraphrase(ph):
    url = "https://api.promptapi.com/paraphraser"

    
    headers= {
    "apikey": "Tkn1WrbppoVq0OsG6zEfA7RG6i80nyQQ"
    }

    response = req.request("POST", url, headers=headers, data = ph)

    status_code = response.status_code
    result = response.text
    print(status_code)
    print(result)

