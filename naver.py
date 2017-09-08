import requests
from bs4 import BeautifulSoup
import pandas as pd

option = {'PBR': 'pbr',
          'PER': 'per',
          'ROA': 'roa',
          'ROE': 'roe',
          '거래대금': 'amount',
          '거래량': 'quant',
          '고가': 'high_val',
          '당기순이익': 'net_income',
          '매도총잔량': 'sell_total',
          '매도호가': 'ask_sell',
          '매수총잔량': 'buy_total',
          '매수호가': 'ask_buy',
          '매출액': 'sales',
          '매출액증가율': 'sales_increasing_rate',
          '보통주배당금': 'dividend',
          '부채총계': 'debt_total',
          '상장주식수': 'listed_stock_cnt',
          '시가': 'open_val',
          '시가총액': 'market_sum',
          '영업이익': 'operating_profit',
          '영업이익증가율': 'operating_profit_increasing_rate',
          '외국인비율': 'frgn_rate',
          '유보율': 'reserve_ratio',
          '자산총계': 'property_total',
          '저가': 'low_val',
          '전일거래량': 'prev_quant',
          '주당순이익': 'eps'}


def get_naver(s=0, p=1, option1='거래량', option2='시가총액', option3='PER', option4='외국인비율', option5='매출액', option6='ROE'):
    '''
    네이버 시가총액 DATA 가져오기
    s = 0. 코스피, 1. 코스닥
    p = 페이지넘버
    '''

    # 1차 필드조건 조회

    url = (
        'http://finance.naver.com/sise/field_submit.nhn?menu=market_sum&returnUrl=http%3A%2F%2Ffinance.naver.com%2Fsise%2Fsise_market_sum.nhn%3F'
        'sosok%3D{0}%26page%3D{1}&fieldIds={2}&fieldIds={3}&fieldIds={4}&fieldIds={5}&fieldIds={6}&fieldIds={7}'
    ).format(s, p, option[option1], option[option2], option[option3], option[option4], option[option5], option[option6])

    r = requests.post(url)
    soup = BeautifulSoup(r.content, 'lxml')
    table = soup.find_all('table')
    df = pd.read_html(str(table[1]))[0]

    return df