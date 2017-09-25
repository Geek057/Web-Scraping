#! /usr/bin/python3
import re
import json
import sys
import requests
import urllib.request

def getouripinfo(ipinfo=''):
    if ipinfo=='':
        url = 'https://ipinfo.io/json'
    else:
        url = 'https://ipinfo.io/' + ipinfo + '/json'

    data = requests.get(url).json()
    IP = data['ip']
    org = data['org']
    city = data['city']
    region = data['region']
    country = data['country']
    postal_code = data['postal']
    location = data['loc']
    print("Your IP Info \n")
    print('IP :  {0} \nCity : {1} \nRegion : {2} \nCountry : {3} \nPostal_code : {4} \nLocation : {5} \nOrg : {6}\n'.format(IP,city,region,country,postal_code,location,org))



if __name__=='__main__':
    while(1):
        print('Enter 1 to get our ip info ')
        print('Enter 2 if you have other IP')
        num = int(input())
        if num==1 or num==2:
            if num==1:
                getouripinfo()
            else:
                try:
                    print('Enter IP')
                    ip_addr = input()
                    match = re.search('^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$', ip_addr)
                    lis = []
                    for i in match.groups():
                       lis.append(int(i))
                    chk = False
                    for num in lis:
                       if num > 255 and num < 0:
                          chk = True
                          break
                    if chk:
                        print('Invalid IP :')
                        continue
                    else:
                        getouripinfo(ip_addr)

                except Exception as f:
                    print("Invalid IP")
            sys.exit()
        else:
            print('Enter Wrong Key')
            print('--------------------')
            continue


