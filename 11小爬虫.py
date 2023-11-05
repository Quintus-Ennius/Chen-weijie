# 从Response对象开始，分成两条路径，一条路径是数据放在HTML里，用BeautifulSoup库去解析数据和提取数据；
# 另一条，数据作为Json存储起来，用response.json()方法去解析，然后提取、存储数据。
"""
# 获取菜谱
import requests # 调用requests库
from bs4 import BeautifulSoup
url = 'https://www.xiachufang.com/explore/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.78'}
res = requests.get(url,headers = headers)
print(res.status_code)
a = res.text
LI=[]
soup = BeautifulSoup(a, 'html.parser')
food_list = soup.find_all('div', class_="info pure-u")
for food in food_list:
    name = food.find('a')
    need1 = name['href']
    url = 'http://www.xiachufang.com'+need1
    Need = food.find('p',class_='ing ellipsis')
    LI.append([name.text[17:-13],url,Need.text[1:-1]])
print(LI)
"""
"""
爬取豆瓣电影Top250并写入Excel文件
import requests, random, bs4,openpyxl
wb=openpyxl.Workbook()
b = wb['Sheet']
b.title='榜单'
b['A1']='排名'
b['B1']='电影名'
b['C1']='推荐语'
b['D1']='评分'
b['E1']='链接'
for x in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.78'}
    res = requests.get(url,headers = headers)
    bs = bs4.BeautifulSoup(res.text, 'html.parser')
    bs = bs.find('ol', class_="grid_view")
    for titles in bs.find_all('li'):
        num = titles.find('em',class_="").text
        #查找序号
        title = titles.find('span', class_="title").text
        #查找电影名
        tes = titles.find('span', class_="inq")
        # 查找推荐语
        if tes == None:#没有推荐语时运行
            comment = titles.find('span',class_="rating_num").text
            #查找评分
            url_movie = titles.find('a')['href']
            print(num + '.' + title + '——' + comment +'\n' + url_movie)
            b.append([num,title,comment,' ',url_movie])
        else:
            a = tes.text
            # 查找推荐语
            comment = titles.find('span', class_="rating_num").text
            # 查找评分
            url_movie = titles.find('a')['href']
            print(num + '.' + title + '——' + comment + '\n' + '推荐语：' + a + '\n' + url_movie)
            b.append([num, title, comment, a,url_movie])
wb.save(r'E:\文件\豆瓣电影排名.xlsx')
"""
"""
下载视频
import time,requests
from bs4 import BeautifulSoup
url1 = 'https://vod.afdiancdn.com/7f76b4e7vodtransbj1256217904/9527f8233701925921421654098/v.f100840.mp4?t=6130bd93&us=612f6c1333bfe&sign=bafda1b817828644cea997aae5b93a2f'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84'}
res = requests.get(url1,headers = headers)
# res.encoding = None
# print(res.content)
with open('C:\\Users\\cwj15\\Desktop\\test\\abc.mp4','wb') as file1:
    file1.write(res.content)
"""
"""
#爬取qq音乐的歌曲信息
import requests
url='https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.top&searchid=57945254974137613&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w=%E5%BC%A0%E6%9D%B0&_=1630219297040&cv=4747474&ct=24&format=json&inCharset=utf-8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&uin=0&g_tk_new_20200303=5381&g_tk=5381&hostUin=0&loginUin=0'
res_music = requests.get(url)
json_music = res_music.json()
list_music = json_music['data']['song']['list']
for music in list_music:
    print(music['name']+' 专辑名：',end='')
    print(music['album']['name'],end=' ')
    print('时长：'+str(music['interval'])+'s',end=' ')
    print('播放链接:'+'https://y.qq.com/n/ryqq/songDetail/'+music['mid'])
    

import requests

# 引用requests模块
url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
for x in range(5):
#爬取5页歌曲信息
    params = {
        'ct': '24',
        'qqmusic_ver': '1298',
        'new_json': '1',
        'remoteplace': 'sizer.yqq.song_next',
        'searchid': '64405487069162918',
        't': '0',
        'aggr': '1',
        'cr': '1',
        'catZhida': '1',
        'lossless': '0',
        'flag_qc': '0',
        'p': str(x + 1),
        'n': '20',
        'w': '周杰伦',
        'g_tk': '5381',
        'loginUin': '0',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'utf-8',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0'
    }
    # 将参数封装为字典
    res_music = requests.get(url, params=params)
    json_music = res_music.json()
    # 使用json()方法，将response对象，转为列表/字典
    list_music = json_music['data']['song']['list']
    # 一层一层地取字典，获取歌单列表
    for music in list_music:
        # list_music是一个列表，music是它里面的元素
        print(music['name'])
        # 以name为键，查找歌曲名
        print('所属专辑：' + music['album']['name'])
        # 查找专辑名
        print('播放时长：' + str(music['interval']) + '秒')
        # 查找播放时长
        print('播放链接：https://y.qq.com/n/yqq/song/' + music['mid'] + '.html\n\n')
        # 查找播放链接
"""
"""
自动登录CSDN社区(有滑块验证时不行)
from selenium import webdriver
import time,requests,json
options = webdriver.ChromeOptions()
options.add_argument('--headless')
# driver = webdriver.Edge('E:\python\msedgedriver.exe')
driver = webdriver.Chrome()
driver.get("https://blog.csdn.net/mkgdjing/article/details/87776319")
driver.implicitly_wait(5)
a = driver.find_element_by_partial_link_text('登录')
a.click()
driver.implicitly_wait(3)
b = driver.find_element_by_partial_link_text('账号密码登录')
b.click()
c = driver.find_element_by_id('all')
c.send_keys('15916278753')
driver.implicitly_wait(2)
d = driver.find_element_by_id('password-number')
d.send_keys('cwj13539559395')
time.sleep(3)
e = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/div[3]/div/div[6]/div/button')
e.click()
cookies = driver.get_cookies()
for cook in cookies:
    cook['domain']='csdn.net'
f1 = open("C:\\Users\\cwj15\\Desktop\\test\\cookies.txt","w")
f1.write(json.dumps(cookies))
f1.write('\r\n'')#换行
f1.close
time.sleep(3)

driver = webdriver.Edge('E:\python\msedgedriver.exe')
driver.delete_all_cookies()
driver.get("https://blog.csdn.net/mkgdjing/article/details/87776319")
time.sleep(5)
f2 = open("C:\\Users\\cwj15\\Desktop\\test\\cookies.txt")
cookies = json.loads(f2.read())
for cook in cookies:
    driver.add_cookie(cook)
driver.refresh()#刷新
time.sleep(2)
"""
"""
从网上爬取当天天气信息并自动发送邮件(要程序处于一直运行状态，才能长久保持)
import time,requests,smtplib
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.header import Header
import schedule
def wea_spider():
    url1 = 'http://www.weather.com.cn/weather1d/101280704.shtml#search'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84'}
    weather = requests.get(url1,headers = headers)
    weather.encoding = 'utf-8'
    weather.text
    bs = BeautifulSoup(weather.text,'html.parser')
    wea = bs.find('p',class_='wea')
    tem = bs.find('p',class_='tem')
    print(wea.text+tem.text[:-1])
    return wea,tem
username = '1261957909@qq.com'
password = 'tyfsedfyncsvjchc'
to_addr = 'cwj15916278753@163.com'
def send_email(wea,tem):
    host = 'smtp.qq.com'
    port = 465
    text = print('今天天气是：'+wea.text+'温度是'+tem.text[:-1])
    msg = MIMEText(text, 'plain','utf-8')
    msg['From'] = Header('python')
    msg['To'] = Header(to_addr)
    msg['Subject'] = Header('天气')
    server = smtplib.SMTP_SSL(host)
    server.connect(host, port)
    server.login(username, password)
    try:
        server.sendmail(username, to_addr, msg.as_string())
        print('邮件发送成功')
    except:
        print('邮件发送失败')
    server.quit()
def job():
    print('开始工作')
    wea,tem = wea_spider()#把这个函数内部return的两个变量tem、wea赋值给job()函数里面的变量tem，wea
    send_email(wea,tem)
    print('任务完成')
schedule.every().day.at("19:20").do(job)
while True:
    schedule.run_pending()

"""
"""
爬取食物热量表并写入excel
from gevent import monkey
monkey.patch_all()
import gevent, requests, openpyxl
from gevent.queue import Queue
from bs4 import BeautifulSoup
url_list = []
for a in range(2, 12):
    if a < 11:
        for b in range(2, 11):
            url = 'http://www.boohee.com/food/group/'+str(a)+'?page='+str(b)
            url_list.append(url)
    else:
        for b in range(2,11):
            url = 'http://www.boohee.com/food/view_menu'+'?page='+str(b)
            url_list.append(url)
work=Queue()
food = {}
for url in url_list:
    work.put_nowait(url)
def crawler():
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84'}
    while not work.empty():
        url = work.get_nowait()
        food_list = requests.get(url,headers = headers)
        html = food_list.text
        soup = BeautifulSoup(html, 'html.parser')
        foods = soup.find_all('li', class_='item clearfix')
        for f in foods:
            url = f.find_all('a')[1]['href']
            title = f.find_all('a')[1]['title']
            hot = f.find('p')
            food[title] = ['链接：'+url,hot.text]
tasks_list = []
for i in range(5):
    task = gevent.spawn(crawler)
    tasks_list.append(task)
gevent.joinall(tasks_list)
a = openpyxl.Workbook()
b = a.active
b.title = '食物热量'
b['A1'] = '食物'
b['B1'] = '链接'
b['C1'] = '热量'
for f in food:
    b['A'+str(list(food).index(f)+2)].value = f
    b['B'+str(list(food).index(f)+2)].value = food[f][0]
    b['C' + str(list(food).index(f)+2)].value = food[f][1]
a.save('C:\\Users\\cwj15\\Desktop\\test\\食物热量表.xlsx')
"""
"""
爬取小说
import requests
from bs4 import *
from selenium import webdriver
import time
options = webdriver.ChromeOptions()
options.add_argument('--headless') # 把Chrome浏览器设置为静默模式,好像爬取不到css元素？
driver = webdriver.Chrome(options = options) # 设置引擎为Chrome，在后台默默运行
url = 'https://www.xbiquge.la/87/87550/'
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47'}
driver.get(url)
driver.implicitly_wait(3)
a=driver.find_element_by_id('list')
title = driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[1]/h1')
li=a.find_elements_by_tag_name('a')
url_list=[]
for i in li:
    url = i.get_attribute('href')
    url_list.append(url)
content_list = []
title_list = []
f1 = open("C:\\Users\\cwj15\\Desktop\\test\\"+title.text+".txt","w",encoding = 'utf-8')
for url in url_list:
    driver.get(url)
    time.sleep(3)
    b = driver.find_element_by_id('content')
    c = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[2]/h1')
    content = b.text.replace(" ", "")
    title = c.text.replace(" ", "")
    content_list.append(content)
    title_list.append(title)
    for title in title_list:
        f1.write(title)
        f1.write('\n')
        for content in content_list:
            f1.write(content)
f1.close
driver.quit()
"""
"""
B站热门视频信息
import requests
from bs4 import *
from selenium import webdriver
import time
options = webdriver.ChromeOptions()
options.add_argument('--headless') # 把Chrome浏览器设置为静默模式,好像爬取不到css元素？
driver = webdriver.Chrome() 
url = 'https://www.bilibili.com/v/popular/all'
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47'}
driver.get(url)
driver.refresh()
time.sleep(3)
for i in range(5):
    time.sleep(3)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
li=driver.find_elements_by_class_name('video-card')
info = {}
for i in li:
    a=i.find_element_by_tag_name('a')
    url = a.get_attribute('href')
    title = i.find_element_by_class_name('video-name')
    up = i.find_element_by_class_name('up-name')
    player = i.find_element_by_class_name('play-text')
    like = i.find_element_by_class_name('like-text')
    info[title.text] = {'up主':up.text,'播放量':player.text,'弹幕数':like.text,'链接':url}
for i in info.keys():
    print(i,end=': ')
    print(info[i])
time.sleep(2)
driver.quit()
"""
"""
#爬取图片
import requests
from bs4 import BeautifulSoup
import re
import random
import time
import os
user_agent_list = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        ]
ip_list = []
def ip_get():
    url='http://www.xiladaili.com/'
    res = requests.get(url)
    soup = BeautifulSoup(res.text,'html.parser')
    a = soup.find('tbody')
    b = a.find_all('tr')
    for c in b:
        ip = c.find('td')
        ip_list.append(ip.text)
def get(url,timeout,proxy=None, num_retries=6):
    value = random.choice(user_agent_list)+' Edg/93.0.961.52'
    headers = {'user-agent':value}
    if proxy == None:
        try:
            return requests.get(url, headers=headers, timeout=timeout)  ##这样服务器就会以为我们是真的浏览器了
        except:  ##如果上面的代码执行报错则执行下面的代码
            if num_retries > 0:  ##num_retries是我们限定的重试次数
                time.sleep(10)  ##延迟十秒
                print(u'获取网页出错，10S后将获取倒数第：', num_retries, u'次')
                return get(url, timeout, num_retries - 1)  ##调用自身 并将次数减1
            else:
                print(u'开始使用代理')
                time.sleep(10)
                ip_get()
                IP = str(random.choice(ip_list)).strip()  ##下面有解释哦
                proxy = {'http': IP}
                return get(url, timeout, proxy)  ##代理不为空的时候
    else:  ##当代理不为空
        try:
            ip_get()
            IP = str(random.choice(ip_list)).strip() #
            proxy = {'http': IP}  ##构造成一个代理
            return requests.get(url, headers=headers, proxies=proxy, timeout=timeout)  ##使用代理获取response
        except:
            if num_retries > 0:
                time.sleep(10)
                ip_get()
                IP = str(random.choice(ip_list)).strip()
                proxy = {'http': IP}
                print(u'正在更换代理，10S后将重新获取倒数第', num_retries, u'次')
                print(u'当前代理是：', proxy)
                return get(url, timeout, proxy, num_retries - 1)
            else:
                print(u'代理也不好使了！取消代理')
                return get(url, 3)
url_list1=[]
def get_img():
    html = get('https://unsplash.com/',3).text
    li = BeautifulSoup(html,'html.parser').find_all(class_="_2Mc8_")
    for a in li:
        href = a['href']
        url = 'https://unsplash.com'+str(href)
        url_list1.append(url)
    return url_list1
url_list2 = []
res_list = []
def download():
    get_img()
    try:
        for url in url_list1:
            html = get(url,3).text
            href = BeautifulSoup(html, 'html.parser').find(class_="_1g5Lu _2gKr0")
            url = href.find('img')['src']
            url_list2.append(url)
        for url in url_list2:
            res = get(url,3).content
            res_list.append(res)
        return res_list
    except AttributeError:
        print('到头了')
def save():
    download()
    if not os.path.exists(r'C:\Users\cwj15\Desktop\test\image'):
        os.mkdir(r'C:\Users\cwj15\Desktop\test\image')
    else:
        print('文件夹已存在')
    i = 0
    for res in res_list:
        f = open('C:\\Users\\cwj15\\Desktop\\test\\image\\'+str(i)+'.jpg','wb')
        f.write(res)
        f.close
        i += 1
save()

"""
"""
12306抢票
from selenium import webdriver
import requests, re, time, json
date = input("请输入你需要查询的日期，以2021-10-26的格式输入：")
start = input("请输入出发地：")
end = input("请输入目的地；")
stations = {}
with open('C:\\Users\\cwj15\\Desktop\\test\\stations1.txt',encoding = 'utf-8') as f1:
    station = f1.readlines()
    for i in station:
        i1 = re.findall('[\u4e00-\u9fa5]+',i)
        i2 = re.findall('[A-Z]+',i)
        for i3 in i1:
            stations[i3] = i2[i1.index(i3)]
if start and end in stations.keys():
    start2 = stations[start]
    end2 = stations[end]
url = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs='+start+','+start2+'&ts='+end+','+end2+'&date='+date+'&flag=N,N,Y'
# url1 = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E7%8F%A0%E6%B5%B7,ZHQ&ts=%E5%B9%BF%E5%B7%9E,GZQ&date=2021-11-02&flag=N,N,Y'
# url2 = 'https://www.12306.cn/index/'
options = webdriver.ChromeOptions() # 实例化Option对象
# options.add_argument('user-agent=""Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
# 添加请求头
# options.add_argument('--headless') # 把Chrome浏览器设置为静默模式,好像爬取不到css元素？
driver = webdriver.Chrome(options = options)
# driver.delete_all_cookies()
driver.get(url)
confirm = driver.find_element_by_id('qd_closeDefaultWarningWindowDialog_id')
confirm.click()
driver.implicitly_wait(1)
# with open("C:\\Users\\cwj15\\Desktop\\test\\12306_cookies.txt") as f3:
#     cookies = json.loads(f3.read())
#     for cook in cookies:
#         driver.add_cookie(cook)
# driver.implicitly_wait(1)
# driver.get(url1)

# login = driver.find_element_by_id('J-btn-login')
# login.click()
# input('输入回车以确认登陆：')
# cookies = driver.get_cookies()
# for cook in cookies:
#     cook['domain'] = '12306.cn'
# with open("C:\\Users\\cwj15\\Desktop\\test\\12306_cookies.txt","w") as f2:
#     f2.write(json.dumps(cookies))
#     f2.write('\r\n')

buttons = []
button = driver.find_elements_by_class_name('btn72')
for i in button:
    buttons.append(i.text)

tm = []
times = driver.find_elements_by_class_name('cds')
for time in times:
    tm.append('出发时间：'+ time.text[:5] + ' 到达时间：' + time.text[-5:])

names = []
name = driver.find_elements_by_class_name('number')
for i in name:
    names.append(i.text)

info = driver.find_element_by_id('queryLeftTable')
a = info.find_elements_by_tag_name('tr')
id_list = []
for id in a:
    str1 = id.get_attribute('id')
    number = re.findall("et.\d.\w{5,10}", str1)
    for id in number:
        id_list.append(id[3:])

infos = {}
def get_info():
    for i in range(len(id_list)):
        if "G" in id_list[i][5:9]:
            infos[names[i] + '商务座特等座'] = "SWZ_"+ id_list[i]
        elif "D7134" in id_list[i][5:10]:
            infos[names[i] + '商务座特等座'] = "SWZ_"+ id_list[i]
        else:
            infos[names[i] + '商务座特等座'] = "TZ_" + id_list[i]
        infos[names[i] +'一等座'] = "ZY_" + id_list[i]
        infos[names[i] +'二等座二等包座'] = "ZE_" + id_list[i]
        infos[names[i] + '高级软卧'] = "GR_" + id_list[i]
        infos[names[i] + '软卧一等卧'] = "RW_" + id_list[i]
        infos[names[i] + '动卧'] = "SRRB_" + id_list[i]
        infos[names[i] + '硬卧二等卧'] = "YW_" + id_list[i]
        infos[names[i] + '软座'] = "RZ_" + id_list[i]
        infos[names[i] + '硬座'] = "YZ_" + id_list[i]
        infos[names[i] + '无座'] = "WZ_" + id_list[i]
        infos[names[i] + '其他'] = "QT_" + id_list[i]

def display():
    get_info()
    num = 1
    n = 0
    for i in infos.items():
        num += 1
        c = driver.find_element_by_id(i[1])
        if num % 13 == 0:
            num = 2
            print('  ' + names[(num // 13)+n] + tm[(num // 13)+n])
            n += 1
            print('\r')
            print(i[0] + '：' + c.text, end=' | ')
        else:
            print(i[0] + '：' + c.text, end=' | ')
    print('  ' + names[-1] + tm[-1])
def buy():
    answer = input('想定哪班车：')
    if answer in names:
        info2 = driver.find_element_by_id('queryLeftTable')
        a2 = info2.find_elements_by_tag_name('tr')
        for id2 in a2:
            str2 = id2.get_attribute('id')
            try:
                if answer == 'G1301':
                    answer = 'G1304'
                    if answer in str2:
                        but = id2.find_element_by_class_name('btn72')
                        but.click()
                else:
                    if answer in str2:
                        but = id2.find_element_by_class_name('btn72')
                        but.click()
            except:
                pass
display()
buy()
"""
"""
带cookies登录买手办
import time
from selenium import webdriver
import re,json
url = 'https://mall.bilibili.com/detail.html?noTitleBar=1&from=shoppingcart#goFrom=na&itemsId=10014574&shopId=2233'
options = webdriver.ChromeOptions() # 实例化Option对象
options.add_argument('--headless') # 把Chrome浏览器设置为静默模式,好像爬取不到css元素？
driver = webdriver.Chrome()
for i in range(5):
    driver.delete_all_cookies()
    driver.get(url)
    f2 = open("C:\\Users\\cwj15\\Desktop\\test\\bili_cookies.txt")
    cookies = json.loads(f2.read())
    for cook in cookies:
        driver.add_cookie(cook)
    driver.implicitly_wait(2)
    buy1 = driver.find_element_by_xpath("/html/body/div/div/div/div[5]/div/div[3]/div[2]/div")
    buy1.click()
    determine = driver.find_element_by_xpath('/html/body/div/div/div/div[8]/div[1]/div/div[3]/div[3]/div')
    determine.click()
    if i == 0:
        buy2 = driver.find_element_by_class_name("dot")
        buy2.click()
    buy3 = driver.find_element_by_class_name("pay-btn")
    buy3.click()
# input('请回车登录')
# cookies = driver.get_cookies()
# for cook in cookies:
#     cook['domain']='bilibili.com'
# f1 = open("C:\\Users\\cwj15\\Desktop\\test\\bili_cookies.txt","w")
# f1.write(json.dumps(cookies))
# f1.write('\r\n')
# f1.close
# time.sleep(3)
"""
"""
定时抢手办
import time, datetime
from datetime import date
from selenium import webdriver
import re,json
times = "2021-11-11 00:30:00.000000"
t = (2021, 11, 11, 0, 30, 0, 3, 315, 0)
a = time.mktime(t)
url1 = 'https://passport.bilibili.com/login?gourl=https%3A%2F%2Fmall.bilibili.com%2Forderlist.html%3FnoTitleBar%3D1%26hashstatus%3D3'
url2 = 'https://mall.bilibili.com/detail.html?noTitleBar=1&from=shoppingcart#goFrom=na&itemsId=10056125&shopId=2233'
options = webdriver.ChromeOptions() # 实例化Option对象
options.add_argument('--headless') # 把Chrome浏览器设置为静默模式,好像爬取不到css元素？
driver = webdriver.Chrome()
# for i in range(5):
driver.delete_all_cookies()
driver.get(url1)
f2 = open("C:\\Users\\cwj15\\Desktop\\test\\bili_cookies.txt")
cookies = json.loads(f2.read())
for cook in cookies:
    driver.add_cookie(cook)
driver.get(url2)
# driver.implicitly_wait(2)
while True:
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    print(now)
    # if now > times:
    #     while True:
    #         try:
    #             if driver.find_element_by_class_name('bottom-buy-remind'):
    #                driver.find_element_by_class_name('bottom-buy-remind').click()
    #         except:
    #             pass
    # determine = driver.find_element_by_xpath('/html/body/div/div/div/div[8]/div[1]/div/div[3]/div[3]/div')
    # determine.click()
    # if i == 0:
    #     buy2 = driver.find_element_by_class_name("dot")
    #     buy2.click()
    # buy3 = driver.find_element_by_class_name("pay-btn")
    # buy3.click()
# input('请回车登录')
# cookies = driver.get_cookies()
# for cook in cookies:
#     cook['domain']='bilibili.com'
# f1 = open("C:\\Users\\cwj15\\Desktop\\test\\bili_cookies.txt","w")
# f1.write(json.dumps(cookies))
# f1.write('\r\n')
# f1.close
# time.sleep(3)
"""