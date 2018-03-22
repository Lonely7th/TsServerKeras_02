#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'JN Zhang'
__mtime__ = '2018/3/22'
"""
import os
import bs4
from time import sleep

import requests

from k_data.k_logs.logs_manager import LogsManager

base_path = os.path.abspath(os.path.join(os.getcwd(), ".."))


def creat_base_files():
    path_file_code = base_path + "/k_data/data_code.txt"
    file_code = open(path_file_code)

    print(path_file_code)
    pass


# 从指定位置开始爬取数据
def start_spider():
    path_file_code = base_path + "/k_data/data_code.txt"
    file_code = open(path_file_code)
    pass


def get_url(self, year, season):
    code_list = self.dm.find_by_id("")
    for item in code_list[:50]:
        key = item["code"][:6]
        url = "http://quotes.money.163.com/trade/lsjysj_" + key + ".html?year=" + year + "&season=" + season
        # 请求失败后重新请求(最多8次)
        max_try = 8
        for tries in range(max_try):
            try:
                content = requests.get(url)
                self.parse_pager(content.content, item["code"])
                break
            except Exception:
                if tries < (max_try - 1):
                    sleep(2)
                    continue
                else:
                    logger.error("SpiderError：" + key)
    code_list.close()

def parse_pager(self, content, key):
    try:
        _result = self.dm.find_by_id(key)
        timer_list = [x["cur_timer"] for x in _result["price_list"]]
        soup = bs4.BeautifulSoup(content, "lxml")
        parse_list = soup.select("div.inner_box tr")
        for item in parse_list[1:]:
            data = [x.string for x in item.select("td")]
            price = {
                "cur_timer": data[0],
                "cur_open_price": data[1],
                "cur_max_price": data[2],
                "cur_min_price": data[3],
                "cur_close_price": data[4],
                "cur_price_range": data[6],
                "cur_total_volume": data[7],
                "cur_total_money": data[8]
            }
            if price["cur_timer"] not in timer_list:
                self.dm.add_tk_item(key, price)
    except Exception:
        logger.error("SpiderError：" + key)


if __name__ == "__main__":
    logger = LogsManager("spider_error").get_logger()
    start_spider()
    pass
