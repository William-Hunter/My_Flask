#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import imp
import json
from flask import current_app
from flask import Flask
import requests
from bs4 import BeautifulSoup
import random
 
imp.reload(sys)




proxies = {
   'http': 'http://127.0.0.1:7890',
   'https': 'http://127.0.0.1:7890',
}


Headers={
  # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    }

def getHtml(url):
    response=requests.get(url=url,headers=Headers,proxies=proxies)
    result=""
    print(response)
    if 200==response.status_code:
        result= response.text
    else:    
        result= ""
    # print(result)
    return result

def saveLinkList(htmlCode,html_path):
    with open(html_path, 'w') as file:
        file.write(str(htmlCode))
        file.close()


def getLinkList(html_path):
    if html_path is None or ""==html_path:
        pass

    htmlcode=None
    with open(html_path, 'r') as file:
        htmlcode=file.read()
        file.close()

    soup = BeautifulSoup(htmlcode, 'html.parser')
    return soup


LIST = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z' ]

def pickupNumber(length=15):
    # prints a random value from the list
    string=""
    for i in range(0,length):
        string=string+random.choice(LIST)
        
    print(string)
    return string

def isEmpty(obj):
    if obj is None or ""==obj or ""== obj.strip():
        return True
    else: 
        return False


def isNotEmpty(obj):
    return not isEmpty(obj)


def getTitle(url):
    code=getHtml(url)
    if isNotEmpty(code):
        soup = BeautifulSoup(code, 'html.parser')
        title=soup.title.text
    else:
        title=url

    return title


def add(url,title,type,category):
    html_path=selectType(type)
    htmlSoup=getLinkList(html_path)

    css_query="body div#links"
    if category is not None and "" != category:
        css_query=css_query+" div#"+category
    
    current_app.logger.info('css_query:\n'+css_query)

    body=htmlSoup.select_one(css_query)

    id=pickupNumber(25)

    new_div = htmlSoup.new_tag("div",id=id) 
    new_div['class']='link'

    new_a = htmlSoup.new_tag("a",href=url) 
    new_a.string = str(title)
    new_div.append(new_a) 

    new_button = htmlSoup.new_tag("button",type="button",onclick="_2delete('"+id+"')") 
    new_button['class']='del-btn'
    new_button.string = "删除"
    new_div.append(new_button) 

    # new_br = htmlSoup.new_tag("br") 
    # new_div.append(new_br)

    body.append(new_div) 

    saveLinkList(htmlSoup,html_path)


def delete(id,type):
    html_path=selectType(type)
    htmlSoup=getLinkList(html_path)
    
    div=htmlSoup.select_one("body div#"+id)
    if div is not None:
        div.decompose()
        saveLinkList(htmlSoup,html_path)


def selectType(type):
    if type is not None and 'ppp'==type:
        HTML_PATH="/opt/workspace/flask/static/link_keeper.html"
    else:
        HTML_PATH="/opt/workspace/flask/static/link_keeper.html"
    return HTML_PATH


if __name__ == "__main__":
    pickupNumber(20)
