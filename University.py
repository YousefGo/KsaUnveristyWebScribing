import requests
from bs4 import BeautifulSoup
import csv

class University:
    def __init__(self, url , file_name):
        self.url = url #the url of website
        self.file_name = file_name # the file name of csv
        self.continer = [] # continer of data
        self.column=['name', 'city', 'foyear', 'president', 'type', 'websiteUrl'] #column

    def makeRequest(self):
        r = requests.get(self.url)
        self.soup = BeautifulSoup(r.content, 'html5lib')
    def getHtmlDocment(self):
        self.makeRequest()

    def extracData(self):
        self.getHtmlDocment()
          # a list to store unveristy
        table = self.soup.find('table', attrs={'class': 'wikitable'})
        for row in table.findAll('tr'):
            data = {}
            for index, td in enumerate(row.findAll('td')):
                if index == 0:
                    data['name'] = td.get_text()
                elif index == 1:
                    data['city'] = td.get_text()
                elif index == 2:
                    data['foyear'] = td.get_text()
                elif index == 3:
                    data['president'] = td.get_text()
                elif index == 4:
                    data['type'] = td.get_text()
                elif index == 5:
                    data['websiteUrl'] = td.get_text()
            self.continer.append(data)

    def writeData(self):
        self.extracData()
        with open(self. file_name, 'w', newline='', encoding="utf-8") as f:
            w = csv.DictWriter(f,self.column )
            w.writeheader()
            for data in self.continer:
                w.writerow(data)
                print('writnig Data...')
            print('Thanks Yousef ,,, we Done')
Url="https://www.marefa.org/%D9%82%D8%A7%D8%A6%D9%85%D8%A9_%D8%A7%D9%84%D8%AC%D8%A7%D9%85%D8%B9%D8%A7%D8%AA_%D9%88%D8%A7%D9%84%D9%83%D9%84%D9%8A%D8%A7%D8%AA_%D9%81%D9%8A_%D8%A7%D9%84%D8%B3%D8%B9%D9%88%D8%AF%D9%8A%D8%A9/simplified"
unveristyName='uni2.csv'
test =University(Url,unveristyName);
test.writeData();