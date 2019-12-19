#导入需要的库
import requests
import re
import csv
import time

#定义爬虫类
class Jobspyder :

    #初始化函数
    def __init__(self,url,headers,pos,csv_name,page_num,fieldnames) :

        self.url = url
        self.nexturl = url
        self.headers = headers
        self.pos = pos
        self.csv_name = csv_name
        self.page_num = page_num
        self.fieldnames = fieldnames
        self.data = []
        

    def getData(self) : #该函数用于获取网页数据并将每一个职位的信息以字典的形式储存在列表中。
        
        response = requests.get(self.nexturl,headers = self.headers) #请求网页
        html = response.content.decode('GBK','ignore') #将网页从二进制数据，根据GBK编码方式返回。
        reg = re.compile(self.pos,re.S) #根据数据的位置来匹配
        items = re.findall(reg,html) #找到职位信息
        for item in items : #将职位储存在列表中
            
            d = {
                    "职位" : item[0],
                    "工作单位" : item[1],
                    "工作地点" : item[2],
                    "薪酬" : item[3],
                    "日期" : item[4]
                }
            self.data.append(d)


    def nextUrl(self,num) : #得到下一个网页的url
        self.nexturl = self.url
        self.nexturl = self.nexturl.format(str(num))

    def csv_writer(self,data): #将得到的存有信息的列表写入到csv文件中。
        with open (self.csv_name,'a+',encoding='GBK',newline='') as f :
            writer = csv.DictWriter(f,fieldnames = fieldnames)
            for datas in data :
                writer.writerow(datas)
            self.data = []


    def run(self) : #运行
        try:
            for num in range(1,self.page_num) :
                time.sleep(2)
                self.nextUrl(num)
                self.getData()
                self.csv_writer(self.data)
            print("爬取成功！")
        except ConnectionError:
            print('链接失败！')







python_csv_name = 'python.csv'
java_csv_name = 'java.csv'
pos = r'class="t1 ">.*? <a target="_blank" title="(.*?)".*? <span class="t2"><a target="_blank" title="(.*?)".*?<span class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>.*? <span class="t5">(.*?)</span>'
python_url ='http://search.51job.com/list/000000,000000,0000,00,9,99,python,2,{}.html'
java_url = 'http://search.51job.com/list/000000,000000,0000,00,9,99,java,2,{}.html'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
fieldnames = ["职位","工作单位","工作地点","薪酬","日期"]
python= Jobspyder(python_url,header,pos,python_csv_name,3,fieldnames)
java = Jobspyder(java_url,header,pos,java_csv_name,3,fieldnames)
python.run()
java.run()