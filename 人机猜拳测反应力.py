import easygui
import sys,random,time,datetime
import pandas as pd
dc = ['石头','剪刀','布']
js = int(input("输入1开始测试："))
sumli = {}
ili = {}
score = {}
sum1 = {}
sum2 = {}
e = 0
c = 0
k = 0 #游玩局数
while js == 1:
    zu = easygui.msgbox("反应力测试"+'第'+str(k+1)+'局')
    i=0 #过招次数
    r=0 #玩家胜利次数
    j=0 #电脑胜利次数
    sum = 0 #反应用时
    b = 3
    while i<=9:
        a=random.randint(0,2)
        if a!=b:
            date_start = pd.to_datetime(datetime.datetime.now())
            reply = easygui.buttonbox('电脑出\n'+dc[a],'人机反应力pk',choices=dc)
            date_end = pd.to_datetime(datetime.datetime.now())
            date_start_end = date_end - date_start #获取反应时间
            if(a==0 and reply ==dc[0])or(a==1 and reply ==dc[1])or(a==2 and reply ==dc[2]):
                r+=0
                j+=0
            elif (a==0 and reply ==dc[2])or(a==1 and reply ==dc[0])or(a==2 and reply ==dc[1]):
                r += 1
                j += 0
            elif (a==0 and reply ==dc[1])or(a==1 and reply ==dc[2])or(a==2 and reply ==dc[0]):
                r += 0
                j += 1
            i = i+1
        b=a
        sum += date_start_end.total_seconds()
    k += 1
    sumli["第" + str(k) + "次总时间"] = sum
    ili["第" + str(k) + "次平均时间"] = sum / i
    score["第" + str(k) + "次总分"] = r
    if r>j:
        zu=easygui.msgbox('总轮次：'+str(i)+'电脑得分：'+str(j)+'您的得分：'+str(r)+'总用时：'+str(sum)+'平均用时：'+str(sum/i)+'恭喜！您赢了！')
    elif r==j:
        zu=easygui.msgbox('总轮次：'+str(i)+'电脑得分：'+str(j)+'您的得分：'+str(r)+'总用时：'+str(sum)+'平均用时：'+str(sum/i)+'平局！')
    else:
        zu=easygui.msgbox('总轮次：'+str(i)+'电脑得分：'+str(j)+'您的得分：'+str(r)+'总用时：'+str(sum)+'平均用时：'+str(sum/i)+'电脑赢了！')
    tc=easygui.buttonbox('再来一局？','反应力测试程序',['是','否'])
    if tc=='是':
        js=1
    else:
        js=0
        break
for i in sumli.values():
    e += i
for i in ili.values():
    c += i
sum1["三次总平均时长："]=c/3
sum2["三次总时长："]=e
print(sumli)
print(ili)
print(sum2)
print(sum1)
print(score)
input("输入回车结束：")