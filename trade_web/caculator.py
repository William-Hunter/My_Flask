#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import imp
import json
from flask import current_app

imp.reload(sys)


STOCKS_JSON_PATH="/opt/workspace/flask/trade_web/stocks.json"


def two2seven(spread,extremly_low):
    stock={}    
    stock['buy_point']=round(extremly_low+spread*2/10.0,2)
    stock['sell_point']=round(extremly_low+spread*7/10.0,2)
    return stock

def three_seven(spread,extremly_low):
    stock={}
    stock['buy_point']=round(extremly_low+spread*3/10.0,2)
    stock['sell_point']=round(extremly_low+spread*7/10.0,2)
    return stock

def two_eight(spread,extremly_low):
    stock={}
    stock['buy_point']=round(extremly_low+spread*2/10.0,2)
    stock['sell_point']=round(extremly_low+spread*8/10.0,2)
    return stock

def one2four(spread,extremly_low):
    stock={}
    stock['buy_point']=round(extremly_low+spread*1/4.0,2)
    stock['sell_point']=round(extremly_low+spread*3/4.0,2)
    return stock


def one2six(spread,extremly_low):
    stock={}
    stock['buy_point']=round(extremly_low+spread*1/6.0,2)
    stock['sell_point']=round(extremly_low+spread*5/6.0,2)
    return stock


switch={
    "two2seven": two2seven,
    "three_seven": three_seven,
    "two_eight":two_eight,
    "one2four": one2four,
    "one2six": one2six
}


def caculate_point(stock={},type="ALL"):
    extremly_low=float(stock['extremly_low'])
    spread=float(stock['extrem_high'])-extremly_low
    if "ALL"==type:
        for key,func in switch.items():
            stock[key]=func(spread,extremly_low)
            # print(key,func)
            # print(stock[key])
    else:
        stock[type]=switch[type](spread,extremly_low)
    return stock


def print_stock(stock,switch=True):
    logs=[]
    count=0
    but_pint=0.00
    sell_point=0.00
    print("-------------------------------------------")
    title="股票："+stock["stock_name"]
    if switch:
        print(title)

    log_template="{}\t在{}以下买入\t在{}以上卖出"

    if "two2seven" in stock:
        log=log_template.format("按照20-70规则",stock['two2seven']['buy_point'],stock['two2seven']['sell_point'])        
        if switch:
            print(log)
        logs.append(log)
        count=count+1
        but_pint=but_pint+stock['two2seven']['buy_point']
        sell_point=sell_point+stock['two2seven']['sell_point']
    if "three_seven" in stock:
        log=log_template.format("按照三七开规则",stock['three_seven']['buy_point'],stock['three_seven']['sell_point'])        
        if switch:
            print(log)
        logs.append(log)
        count=count+1
        but_pint=but_pint+stock['three_seven']['buy_point']
        sell_point=sell_point+stock['three_seven']['sell_point']
    if "one2four" in stock:
        log=log_template.format("按照4段规则",stock['one2four']['buy_point'],stock['one2four']['sell_point'])        
        if switch:
            print(log)
        logs.append(log)
        count=count+1
        but_pint=but_pint+stock['one2four']['buy_point']
        sell_point=sell_point+stock['one2four']['sell_point']
    if "two_eight" in stock:
        log=log_template.format("按照二八开规则",stock['two_eight']['buy_point'],stock['two_eight']['sell_point'])        
        if switch:
            print(log)
        logs.append(log)
        count=count+1
        but_pint=but_pint+stock['two_eight']['buy_point']
        sell_point=sell_point+stock['two_eight']['sell_point']
    if "one2six" in stock:
        log=log_template.format("按照6段规则",stock['one2six']['buy_point'],stock['one2six']['sell_point'])        
        if switch:
            print(log)
        logs.append(log)
        count=count+1
        but_pint=but_pint+stock['one2six']['buy_point']
        sell_point=sell_point+stock['one2six']['sell_point']

    log=log_template.format("平均下来",round(but_pint/count,2),round(sell_point/count-0.05,2))
    # log="平均下来,\t最高买点应该是：{}，\t最低卖点应该是：{}".format(round(but_pint/count,2),round(sell_point/count,2))
    if switch:
        print(log)
    logs.append(log)
    return logs


def read2calc():
    stock_list = show_stocks()
    logs=[]
    for stock in stock_list:
        stock=caculate_point(stock)
        # stock=caculate_point(stock,'three_seven')
        stock['log']=print_stock(stock,False)
        logs.append(stock)
    return logs



def readJson():
    f = open(STOCKS_JSON_PATH,'r',encoding='utf-8')
    strr=f.read()
    f.close()
    return json.loads(strr)


def show_stocks():
    return list(readJson().values())

def writeJson(json_str):
    f = open(STOCKS_JSON_PATH, 'w',encoding='utf-8')
    f.write(json_str)
    f.close()

def update_stock(data_str):
    jsonData=json.loads(data_str)
    newStock={}
    newStock['stock_id']=jsonData['stock_id']
    newStock['stock_name']=jsonData['stock_name']
    newStock['extrem_high']=jsonData['extrem_high']
    newStock['extremly_low']=jsonData['extremly_low']
    jsonDict=readJson()
    jsonDict[newStock['stock_id']]=newStock
    writeJson(json.dumps(jsonDict))


def remove_stock(stock_id):
    jsonDict=readJson()
    if stock_id in jsonDict:
        del jsonDict[stock_id]
        writeJson(json.dumps(jsonDict))


def calc_stock(stock_id):    
    jsonDict=readJson()
    stock=jsonDict[stock_id]
    stock=caculate_point(stock)
    return print_stock(stock,False)
    



if __name__=="__main__":#测试方法
    read2calc()


