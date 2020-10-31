import requests
from bs4 import BeautifulSoup
import os
if not os.path.exists('./ptthomework'):
    os.mkdir('./ptthomework')
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.51',
           'over18':'1'}
url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
ss = requests.session()
ss.cookies['over18']='1'

n= int(input("請輸入欲爬取的頁數:"))
for i in range(0,n):
    res = ss.get(url, headers=headers,)
    soup = BeautifulSoup(res.text,'html.parser')
    titles = soup.select('div.title a')
    # print(titles)

    for title in titles:

        restitle = title.text # 文章標題

        resurl='https://www.ptt.cc'+title["href"] # 文章個別網址
        # print(resurl)
        resarticle = ss.get(resurl, headers=headers) # 利用個別網址再拿取資料
        souparticle = BeautifulSoup(resarticle.text, 'html.parser') # 利用bs4套件進行解析
        # print(souparticle)
        articles = souparticle.select('div[id="main-content"]')[0].text.split("※ 發信站")[0] # 利用select篩選出標籤id=main-content的內文(第0項資料)
        # print(articles)

        print("===================================================================")
        # articlesp = souparticle.select('div[id="main-content"]')[0].text.split("※ 文章網址")[1]
        # print(articlesp)
        articlesup = souparticle.select('span[class="hl push-tag"]')
        # print("推數:",len(articlespg)) # 推噓數若以tag來篩選會遇到箭頭符號(並不是推或噓)tag也相同,此數有誤差
        articlesdown = souparticle.select('span[class="f1 hl push-tag"]')
        # print("噓數:",len(articlespb))
        a = souparticle.select('div [class="article-metaline"]')[0].text.replace('作者','')
        b = souparticle.select('div [class="article-metaline"]')[1].text.replace('標題','')
        c = souparticle.select('div [class="article-metaline"]')[2].text.replace('時間','')
        d = souparticle.select('div [class="article-metaline-right"]')[0].text.replace('看板','')
        # print("作者:",a)
        # print("標題:",b)
        # print("時間:",c)
        # print("看板:",d)
        # articlesgg = souparticle.select('div[class="push"] span') #此行只是用來檢查推噓數是否與篩選數相同
        # print(articlesgg)
        push_down = 0
        push_up = 0
        for arti in articlesup:
            if "推" in arti.text:
                push_up += 1
        # print("推:",push_up)
        for arti in articlesdown:
            if "噓" in arti.text:
                push_down += 1
        # print("噓:",push_down)
        score = push_up - push_down
        articles += '\n===========split===========\n'
        articles += "推: %s\n" %(push_up)
        articles += "噓: %s\n" %(push_down)
        articles += "分數: %s\n" %(score)
        articles += "作者: %s\n" %(a)
        articles += "標題: %s\n" %(b)
        articles += "時間: %s\n" %(c)
        articles += "看板: %s\n" %(d)
        # print(articles)
        try:
            with open('./ptthomework/%s.txt'%(restitle),'w',encoding='utf-8') as f:
                f.write(articles)
        except FileNotFoundError as e:
            print("這是e:",e)
            with open('./ptthomework/%s.txt'%(restitle.replace('/','').replace(":",'-')),'w',encoding='utf-8') as f:
                f.write(articles)
        except OSError as e2:
            print("這是e2:",e2)
            with open('./ptthomework/%s.txt'%(restitle.replace('/','-').replace('?','-').replace(':','-').replace(' ','-')),'w',encoding='utf-8') as f:
                f.write(articles)

    newurl = 'https://www.ptt.cc'+soup.select('a[class="btn wide"]')[1]['href']
    url = newurl
# r'c:/users/202009-DA02004/Desktop/PYTHON/pyETL