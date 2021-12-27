import requests as req
s='Lamps-Lighting.com is your number one source for buying lighting online. We always show the newest lighting fixtures from all the most popular lighting companies.'
r=s.replace(' ', '%')
res=req.options(f'https://rest.quillbot.com/api/paraphraser/single-flip?text={s}&fthresh=9')
print(res)
print('{}\n{}\r\n{}\r\n\r\n{}'.format(
        '-----------START-----------',
        '\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))