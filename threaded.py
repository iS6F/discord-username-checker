from ext import *
from threading import Thread

def run():
    global r
    while True:
        i = choice(k)
        if r>=8: sleep(8*60) #sleeptime after ratelimitedd
        nl = l(1); nd = d(1)
        n =  a(4)
        t = post('https://discord.com/api/v9/users/@me/pomelo-attempt', headers={'authority': 'discord.com','accept': '*/*','accept-language': 'ar','authorization': i,'cache-control': 'no-cache','content-type': 'application/json','cookie': '__dcfduid=875e9700575311efa68bef39caa63288; __sdcfduid=875e9701575311efa68bef39caa63288de75bc966279540de668e8d261a39404ea322a1417c5592e8f5d6a1343d4bd99; __cfruid=aed401c605781afd6c1a957248eb64dab5c63af9-1723320173; _cfuvid=uBKm6_qBtnJJjyJxwYuNivH6478I_YoXh66CzVHy6QI-1723320173683-0.0.1.1-604800000','origin': 'https://discord.com','pragma': 'no-cache','referer': 'https://discord.com/channels/@me','sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43','x-debug-options': 'bugReporterEnabled', 'x-discord-locale': 'es-ES', 'x-discord-timezone': 'Asia/Riyadh','x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwOS4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzExNS4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTE1LjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MzE3MzkyLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=='}, data=dumps({'username': n}))
        print(n,t.text+i.split('.')[0])
        if t.json() == {'taken': False}: post(web, data={'@everyone'})
        elif 'rate' in t.text: r+=1
        sleep(s)
    post(web, data={'content': 'rate'})
    
for _ in range(5):
    Thread(target=run).start()