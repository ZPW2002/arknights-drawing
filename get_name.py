# -*- coding: UTF-8 -*-
import urllib.request
from bs4 import BeautifulSoup
import re
import openpyxl

def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"
    }
    req = urllib.request.Request(url=url, headers=head)
    response = urllib.request.urlopen(req)
    html = BeautifulSoup(response.read().decode('utf-8'), "html.parser")
    return html


def getName():
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    url = r'http://prts.wiki/w/%E5%B9%B2%E5%91%98%E4%B8%80%E8%A7%88'
    html = askURL(url)

    i = 0
    print('获得名字中...')
    for item in html.find_all('div', class_="smwdata"):
        i += 1
        item_str = str(item)
        cn_name = re.findall(re.compile(r'data-cn="(.*)" data-des'), item_str)[0]
        sheet.cell(i, 1).value = cn_name

    print('名字获取完毕')
    workbook.save('name.xlsx')
