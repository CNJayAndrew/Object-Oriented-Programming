#面向对象数据清洗 不知道为什么数据都没有保存到文件夹里
import re
import csv
import numpy as np


class DataCleaning:
    def __init__(self,filename):
        self.jobName = 0
        self.locality = 0
        self.salary = 0
        self.companyName = 0
        self.releaseTime = 0
        self.data = []
        self.nd_data = 0
        self.minSa=[]
        self.maxSa =[]
        self.newLocality = []
        self.filename = filename


    def readFile(self):
        with open(self.filename,encoding='gbk') as f:
            csv_reader = csv.reader(f) #使用csv.reader读取f中的文件
            data_header = next(csv_reader) #读取第一行每一列的标题
            for row in csv_reader: #将csv文件中的数据保存到data中
                self.data.append(row)
        self.nd_data = np.array(self.data)   #将list数组转化成array数组便于查看数据结构
        self.jobName = self.nd_data[:, 0]  
        self.companyName = self.nd_data[:, 1]  
        self.locality = self.nd_data[:, 2]  
        self.salary = self.nd_data[:, 3]
        self.releaseTime = self.nd_data[:, 4]


    def salaryCleaning(self):
        for sa in self.salary:
            if sa:
                if '-' in sa: #针对1-2万/月或者10-20万/年的情况，包含-
                    minSalary = re.findall(re.compile('(\d*\.?\d+)'),sa)[0]
                    maxSalary = re.findall(re.compile('(\d?\.?\d+)'),sa)[1]
                    if u'万' in sa and u'年' in sa: #单位统一成千/月
                        minSalary = float(minSalary) / 12 *10 
                        maxSalary = float(maxSalary) / 12 *10
                    elif u'万'in sa and u'月' in sa:
                        minSalary = float(minSalary) * 10
                        maxSalary = float(maxSalary) * 10
                else:
                    minSalary = re.findall (re.compile('(\d*\.?\d+)'),sa)[0]
                    maxSalary = ""
                    if u'万' in sa and u'年' in sa:
                        minSalary = float(minSalary) /12 *10
                    elif u'万' in sa and u'月' in sa:
                        minSalary = float(minSalary) *10
                    elif u'元' in sa and u'天' in sa:
                        minSalary = float(minSalary)/1000*21
            else:
                minSalary = ""; maxSalary = "";
            self.minSa.append(minSalary);self.maxSa.append(maxSalary)


    def locFormat(self):
        for loc in self.locality:
            if '-'in loc:#针对有区域的情况，包含-
                newLoc = re.findall(re.compile('(\w*)-'),loc)[0]
            else:#针对没有区域的情况
                newLoc = loc
            self.newLocality.append(newLoc)


    def saveNewFile(self):
        new_f = open('python.csv', 'wt', newline='', encoding='GBK', errors='ignore')
        writer = csv.writer(new_f)
        writer.writerow(('职位', '公司地区','最低薪资(千/月)','最高薪资(千/月)', '公司名称', '发布时间'))
        num = 0  
        while True:
            try:#所有数据都写入文件后，退出循环
               if self.newLocality[num] and self.minSa[num] and self.maxSa[num] and self.companyName[num] and self.newLocality[num]!="异地招聘":
                    writer.writerow((self.jobName[num], self.newLocality[num], self.minSa[num], self.maxSa[num], self.companyName[num], self.releaseTime[num]))
               num += 1
            except Exception:
                break


    def main(self):
    # 获取源数据
      self.readFile()     
     # 清洗源数据中的公司地区和薪资
      self.locFormat ()
      self.salaryCleaning()
    # 将清洗后的数据存入CSV文件
      self.saveNewFile()
      
a = DataCleaning("python.csv")
a.main()