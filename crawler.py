import urllib
import time

from urllib.request import urlopen
from bs4 import BeautifulSoup

stockCode = '065450' # 065450 빅텍

dayPriceUrl = 'http://finance.naver.com/item/sise_day.nhn?code=' + stockCode
dayPriceHtml = urlopen(dayPriceUrl)
dayPriceSource = BeautifulSoup(dayPriceHtml.read(), "html.parser")

dayPricePageNavigation = dayPriceSource.find_all("table", align="center")
dayPriceMaxPageSection = dayPricePageNavigation[0].find_all("td", class_="pgRR")
dayPriceMaxPageNum = int(dayPriceMaxPageSection[0].a.get('href')[-3:])

for page in range(1, dayPriceMaxPageNum + 1):
    url = 'http://finance.naver.com/item/sise_day.nhn?code=' + stockCode + '&page=' + str(page)
    html = urlopen(url)
    source = BeautifulSoup(html.read(), "html.parser")
    srlists = source.find_all("tr")
    isCheckNone = None

    # day: 날짜
    # closingPrice: 종가
    # variation: 전일대비
    # openingPrice: 시가
    # highestPrice: 고가
    # lowestPrice: 저가
    # volume: 거래량

    for i in range(1, len(srlists) - 1):
        if (srlists[i].span != isCheckNone):
            day = srlists[i].find_all("td", align="center")[0].text
            closingPrice = srlists[i].find_all("td", class_="num")[0].text

            srCompareWithYesterday = srlists[i].find("img")
            if (srCompareWithYesterday != None):
                incOrdec = srCompareWithYesterday.get("src")
                absoluteVariation = (srCompareWithYesterday.find("span").text).strip()  # 부호가 포함되지 않은 전일비

                if (incOrdec == "http://imgstock.naver.com/images/images4/ico_down.gif"):
                    variation = '-' + absoluteVariation
                elif (
                        incOrdec == "http://imgstock.naver.com/images/images4/ico_up.gif" or incOrdec == "http://imgstock.naver.com/images/images4/ico_up02.gif"):
                    variation = '+' + absoluteVariation
            else:
                variation = '0'

            openingPrice = srlists[i].find_all("td", class_="num")[2].text
            highestPrice = srlists[i].find_all("td", class_="num")[3].text
            lowestPrice = srlists[i].find_all("td", class_="num")[4].text
            volume = srlists[i].find_all("td", class_="num")[5].text

            print("날짜: " + day, end=" ")
            print("종가: " + closingPrice, end=" ")
            print("전일비: " + variation, end=" ")
            print("시가: " + openingPrice, end=" ")
            print("고가: " + highestPrice, end=" ")
            print("저가: " + lowestPrice, end=" ")
            print("거래량: " + volume)