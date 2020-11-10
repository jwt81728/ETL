import requests
import time
import os
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
if not os.path.exists('./104HW'):
    os.mkdir('./104HW')
# url_a = 'https://www.104.com.tw/jobs/search/?ro=0&keyword=Ai%20%E5%A4%A7%E6%95%B8%E6%93%9A&order=12&asc=0&page'
# url_b = 'mode=l&jobsource=2018indexpoc'
url = 'https://www.104.com.tw/jobs/search/?keyword=Ai%20%E5%A4%A7%E6%95%B8%E6%93%9A&order=1&jobsource=2018indexpoc&ro=0'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.56'}
# ss = requests.session()
# res = ss.get(url,headers=headers)
# for page in range(1,10):
#     url = url_a + str(page) + url_b

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--hide-scrollbars')
chrome_options.add_argument('blink-settings=imagesEnabled=false')
driver = webdriver.Chrome(options=chrome_options)
driver1 = webdriver.Chrome(options=chrome_options)
# driver1 =  Chrome('./chromedriver')
driver1.get(url)
html = driver1.page_source
soup = BeautifulSoup(html,'html.parser')
for i in range(20):
    # driver1.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    # time.sleep(0.6)
    driver1.execute_script('var s = document.documentElement.scrollTop=10000000')
    time.sleep(2)

    all_job_datas=[]
    for title_1 in soup.select('article.js-job-item'):

        title_urls = title_1.select('a.js-job-link')
        for i in title_urls:
            title_url = "https:" + i["href"]
            print(title_url)  # 職缺網址
            title = i.text
            print(title)  # 職缺

            driver = webdriver.Chrome(options=chrome_options)
            # driver = Chrome('./chromedriver')
            driver.get(title_url)
            time.sleep(2)
            html = driver.page_source
            soup2 = BeautifulSoup(html,'html.parser')
            # print(soup2)
            try:
                com_name = soup2.select_one('a[class="btn-link t3 mr-6"]').text.replace(" ",'') # 公司名稱
                # print("公司名稱:",com_name)
                contents = soup2.select('p[class="mb-5 r3 job-description__content text-break"]')  # 工作內容
                for content in contents:
                    print("="*100)
                    # print("工作內容:\n",content.text)
                pay = soup2.select_one('p[class="t3 mb-0 mr-2 monthly-salary text-primary font-weight-bold float-left"]').text.replace(" ","")
                # print("薪資待遇:",pay)  # 薪資待遇
                pla = soup2.select('p[class="t3 mb-0"]')
                # print("工作性質:",pla[0].text.replace(" ", '')) # 工作性質
                # print("工作地點:",pla[1].text.replace(" ", '')) # 工作地點
                # print("管理責任:",pla[2].text.replace(" ", '')) # 管理責任
                # print("出差外派:",pla[3].text.replace(" ", '')) # 出差外派
                # print("上班時段:",pla[4].text.replace(" ", '')) # 上班時段
                # print("休假制度:",pla[5].text.replace(" ", '')) # 休假制度
                # print("可上班日:",pla[6].text.replace(" ", '')) # 可上班日
                # print("需求人數:",pla[7].text.replace(" ", '')) # 需求人數
                need = soup2.select('div[class="col p-0 job-requirement-table__data"]')[0].text
                # print("接受身份:",need) # 接受身份
                exp = soup2.select('div[class="col p-0 job-requirement-table__data"]')[1].text.replace(" ", '')
                # print("工作經歷:",exp) # 工作經歷
                sc = soup2.select('div[class="col p-0 job-requirement-table__data"]')[2].text.replace(" ", '')
                # print("學歷要求:",sc) # 學歷要求
                sc1 = soup2.select('div[class="col p-0 job-requirement-table__data"]')[3].text.replace(" ", '')
                # print("科系要求:",sc1) # 科系要求
                speak = soup2.select('div[class="col p-0 job-requirement-table__data"]')[4].text.replace(" ", '')
                # print("語文條件:",speak) # 語文條件
                tool = soup2.select('div[class="col p-0 job-requirement-table__data"]')[5].text.replace(" ", '')
                # print("擅長工具:",tool) # 擅長工具
                skill = soup2.select('div[class="col p-0 job-requirement-table__data"]')[6].text.replace(" ", '')
                # print("工作技能:",skill) # 工作技能
                try:
                    bonus = soup2.select('p[class="r3 mb-0 text-break"]')[0].text
                    # print("福利:\n",bonus) # 福利
                except:
                    pass
                # print("="*100)
                # title += "\n職缺: %s\n" %(title)
                # title += "聯絡網址: %s\n" %(title_url)
                # title += "公司名稱: %s\n" %(com_name)
                # title += "工作內容: %s\n" %(content.text)
                # title += "薪資待遇: %s\n" %(pay)
                # title += "工作性質: %s\n" %(pla[0].text.replace(" ", ''))
                # title += "工作地點: %s\n" %(pla[1].text.replace(" ", ''))
                # title += "管理責任: %s\n" %(pla[2].text.replace(" ", ''))
                # title += "出差外派: %s\n" %(pla[3].text.replace(" ", ''))
                # title += "上班時段: %s\n" %(pla[4].text.replace(" ", ''))
                # title += "休假制度: %s\n" %(pla[5].text.replace(" ", ''))
                # title += "可上班日: %s\n" %(pla[6].text.replace(" ", ''))
                # title += "需求人數: %s\n" %(pla[7].text.replace(" ", ''))
                # title += "接受身份: %s\n" %(need)
                # title += "工作經歷: %s\n" %(exp)
                # title += "學歷要求: %s\n" %(sc)
                # title += "科系要求: %s\n" %(sc1)
                # title += "語文條件: %s\n" %(speak)
                # title += "擅長工具: %s\n" %(tool)
                # title += "工作技能: %s\n" %(skill)
                # title += "福利:\n %s" %(bonus)
                # print(title)
                job_data = {'職缺': title,'公司名稱': com_name,'工作內容':content.text, '薪資待遇': pay,
                            '工作性質':pla[0].text.replace(" ", ''),'工作地址': pla[1].text.replace(" ", ''),
                            '管理責任':pla[2].text.replace(" ", ''), '出差外派':pla[3].text.replace(" ", ''),
                            '上班時段':pla[4].text.replace(" ", ''),'休假制度':pla[5].text.replace(" ", ''),
                            '可上班日':pla[6].text.replace(" ", ''),'需求人數':pla[7].text.replace(" ", ''),
                            '接受身份':need,'工作經歷':exp,'學歷要求':sc,'科系要求':sc1,'語文條件':speak,'擅長工具':tool,
                            '工作技能':skill,'福利': bonus,'聯絡網址': title_url}
                all_job_datas.append(job_data)

                time.sleep(1)
                fn = '104人力銀行職缺.csv'
                columns_name = ['職缺', '公司名稱', '工作內容','薪資待遇','工作性質','工作地址','管理責任','出差外派',
                                '上班時段','休假制度','可上班日','需求人數','接受身份','工作經歷','學歷要求','科系要求','語文條件',
                                '擅長工具','工作技能','福利','聯絡網址' ]
                with open(fn, 'w', newline='',encoding='utf-8-sig') as csvFile:  # 定義CSV的寫入檔,並且每次寫入完會換下一行
                    dictWriter = csv.DictWriter(csvFile, fieldnames=columns_name)  # 定義寫入器
                    dictWriter.writeheader()
                    for data in all_job_datas:
                        dictWriter.writerow(data)

                time.sleep(1)
            except:
                print("Fail and Try Again!")
            driver.close()

driver1.close()

