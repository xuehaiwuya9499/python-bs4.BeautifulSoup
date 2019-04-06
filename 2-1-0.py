#CalUnivRankingA.py
import requests
from bs4 import BeautifulSoup
import bs4
import time
while True:
    def findMax(ulist,html):
        global maximum
        for li in ulist:
            if len(li[1])>maximum:
                maximum=len(li[1])
    def getHTMLText(url):
        try:
            kv={'user-agent':'Mozilla/5.0'}
            r=requests.get(url,timeout=30,headers=kv)
            print(r.status_code)
            r.raise_for_status
            r.encoding=r.apparent_encoding
            return r.text
        except:
            return ''
    def fillUnivList(ulist,html):
        soup=BeautifulSoup(html,'html.parser')
        try:
            for tr in soup.find('tbody').children:  #遍历tbody中的子孙节点
                if isinstance(tr,bs4.element.Tag):
                    tds=tr('td')  #相当于td.find_all()，返回一个列表
                    ulist.append([tds[0].string,tds[1].string,tds[3].string])  #返回标签中的Navigablestring部分
            return True
        except:
            return False
    def printUnivList(ulist,num):
        global maximum,year
        ti=time.time()
        ti1=str(ti).replace('.','')
        f=open(str(int(year))+'大学排名'+ti1+'.txt','w',encoding='utf-8')
        print(int(year))
        print('{0:^10}\t{1:{3}^{4}}\t{2:^9}'.format('排名','学校名称','总分',chr(12288),maximum))
        f.write('{0:^10}\t{1:{3}^{4}}\t{2:^10}\n'.format('排名','学校名称','总分',chr(12288),maximum))
        flag=True
        if num>len(ulist):
            num=len(ulist)
            flag=False
        for i in range(num):
            u=ulist[i]
            if len(u[1])%2==1:
                print('{0:^10}\t'.format(str(i+1)),end=' ')
                f.write('{0:^10}\t'.format(str(i+1))+' ')
                print('{0:{2}^{3}}\t{1:^10}'.format(u[1],u[2],chr(12288),maximum))
                f.write('{0:{2}^{3}}\t{1:^10}\n'.format(u[1],u[2],chr(12288),maximum))
            else:
                print('{0:^10}\t{1:{3}^{4}}\t{2:^10}'.format(str(i+1),u[1],u[2],chr(12288),maximum))
                f.write('{0:^10}\t{1:{3}^{4}}\t{2:^10}\n'.format(str(i+1),u[1],u[2],chr(12288),maximum))
        if flag==False:
            print('输入大学数量过多，已自动输出前{}所大学排名。'.format(num))
        f.close()
    def main():
        global a,year
        flag=False
        while True:
            lis=[]
            st=input('请输入要输出大学的数量和年份以，分隔：\n')
            #判断输入的数字是不是复数
            if 'j' in st:
                flag=False
            else:
                flag=True
            #分割st字符串
            if ',' in st and flag==True:
                lis=st.split(',')
                flag=True
            elif '，' in st and flag==True:
                lis=st.split('，')
                flag=True
            else:
                print('输入有误，请按照格式输入！')
                flag=False
            #考虑到用户不小心输入多个逗号的情况
            if flag==True:
                while True:
                    if '' in lis:
                        lis.remove('')
                    else:
                        break
                #若用户输入超过两个数字则要求重新输入
                if len(lis)==2:
                    flag=True
                else:
                    flag=False
                #判断输入的两个数字是否合法
                if flag==True:
                    tempa,tempy=lis
                    try:
                        a,year=eval(tempa),eval(tempy)
                        flag=True
                    except:
                        flag=False
            if flag==False:
                continue
            else:
                break
        uinfo=[]
        if int(year)==2015:
            url='http://www.zuihaodaxue.cn/zuihaodaxuepaiming2015_0.html'
        else:
            url='http://www.zuihaodaxue.cn/zuihaodaxuepaiming'+str(int(year))+'.html'
        html=getHTMLText(url)
        if fillUnivList(uinfo,html):
            findMax(uinfo,html)
            printUnivList(uinfo,int(a))
            print('有关大学排名文件已存盘于与本程序相同目录的文件夹内。')
        else:
            print('输入年份无数据！')
    maximum=0
    a,year=0,0
    main()
    t=input('是否退出程序？\n键入y以退出，键入其它字符以继续。\n')
    if t=='y' or t=='Y':
        break
    else:
        continue
    
