import requests
from bs4 import BeautifulSoup
import os
import random ,time
if not os.path.exists('./pic'):
    os.mkdir('./pic')
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.55'}
url_a = "https://www.canstockphoto.com.tw/images-photos/"
# url_b = input('請輸入關鍵字:')
url_b = '水果'
ss = requests.Session()

for page in range(1,4):
    if page == 1 :
        url = url_a+url_b+".html"

    elif page > 1 :
        url = url_a+url_b+"_"+str(page)+".html"

    res = ss.get(url, headers=headers)
    soup = BeautifulSoup(res.text,'html.parser')
    # print(soup)
    # print(soup.text)
    # pi = soup.select('div[class="clearfix"]')['img']
    pi = soup.select('span[class="thumb-container"] img')
    # print(pi)

    for i in pi :
        imgg = i.get(r'src')
        print(imgg)
        image = requests.get(imgg)

        imgg_name = imgg.split('tw/')[1]
        # image = "https://cdn.xl.thumbs.canstockphoto.com.tw/"+imgg_name
        # print(image)
        with open('./pic/%s' % (imgg_name), 'wb+') as f:
            f.write(image.content)
    time.sleep(random.randint(1, 3))
    print('='*100)

