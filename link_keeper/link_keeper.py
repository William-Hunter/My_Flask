#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import imp
import json
from flask import current_app
import requests
from bs4 import BeautifulSoup
import random
 


imp.reload(sys)


HTML_PATH="/opt/workspace/flask/static/link_keeper.html"


Headers={
  # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    }

def getHtml(url):
    response=requests.get(url=url,headers=Headers)
    result=""
    print(response)
    if 200==response.status_code:
        result= response.text

    # print(result)
    return result


def saveLinkList(htmlCode):
    with open(HTML_PATH, 'w') as file:
        file.write(str(htmlCode))



def getLinkList():

    htmlcode=None
    with open(HTML_PATH, 'r') as file:
        htmlcode=file.read()

    soup = BeautifulSoup(htmlcode, 'html.parser')
    return soup


LIST = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z' ]

def pickupNumber():
    # prints a random value from the list
    string=""
    for i in range(0,15):
        string=string+random.choice(LIST)
        
    print(string)
    return string


def add(url,title):
    print("url:",url)

    htmlSoup=getLinkList()
    body=htmlSoup.select_one("body div#links")

    id=pickupNumber()

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

    saveLinkList(htmlSoup)


def delete(id):
    htmlSoup=getLinkList()
    
    div=htmlSoup.select_one("body div#"+id)
    if div is not None:
        div.decompose()
        saveLinkList(htmlSoup)



if __name__ == "__main__":
    pickupNumber()
