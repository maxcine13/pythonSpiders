# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

def readfile(filename):
    with open(filename, 'r') as f:
        return f.read().split('\n')


def readfileString(filename):
    with open(filename, 'r') as f:
        return f.read()


def writefile(filename, string):
    with open(filename, 'a') as f:
        f.write(str(string) + '\n')


def writefilew(filename, string):
    with open(filename, 'w') as f:
        f.write(str(string) + '\n')



def getHtmlSoup(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:48.0) Gecko/20100101 Firefox/48.0"}
    response = requests.get(url, headers=header)
    # response.encoding = 'utf-8'
    text = response.text
    return BeautifulSoup(text, 'html.parser')

