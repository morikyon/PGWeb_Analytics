#!/usr/bin/env python
# coding: utf-8

# library
from urllib import request
from bs4 import BeautifulSoup
import csv
import time

# filename
filename = "programmableweb_list.csv"

def scraping():
    #url
    url_init = "https://www.programmableweb.com/category/all/apis"
    url_page = "https://www.programmableweb.com/category/all/apis?page="
    pgweb_scraping(url_init, True)
    for urlNo in range(1, 786):
        url_page += str(urlNo)
        pgweb_scraping(url_page, False)
        time.sleep(0.5)

def pgweb_scraping(url, header):
    # url: URL
    # header: True --> Add header
    #       False --> no header
    #get html
    html = request.urlopen(url)
    #set BueatifulSoup
    soup = BeautifulSoup(html, "html.parser")
    #get table
    programmableweb = soup.find("table", attrs={"class", "views-table cols-4 table"})
    programmableweb_rows = programmableweb.find_all("tr")

    # Write csv Header
    if header == True:
        write2Csv(programmableweb_rows ,True)
    write2Csv(programmableweb_rows ,False)

def write2Csv(rows, th):
    with open(filename, 'a', newline = '', encoding = 'utf-8') as f:
        writer = csv.writer(f)
        for row in rows:
            csvRow = []
            if th == True:
                for cell in row.find_all("th"):
                    csvRow.append(cell.get_text())
                if len(csvRow) > 0:
                    writer.writerow(csvRow)
            else:
                for cell in row.find_all("td"):
                    csvRow.append(cell.get_text())
                if len(csvRow) > 0:
                    writer.writerow(csvRow)

if __name__ == "__main__":
    scraping()



