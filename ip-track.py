#!/usr/bin/python3

import requests
from argparse import ArgumentParser
import json

parser = ArgumentParser(description="This tool is used to track geo-location of given ip-address "
                                    "or url",epilog="Example : ./ip-track.py -i demo.testfire.net")

rparser = parser.add_argument_group("required argument")

rparser.add_argument("-i","--ip",dest="ip",type=str,help="Type ip-address or url",required=True)

args = parser.parse_args()

ip = args.ip

url = "http://ip-api.com/json/"+ip

res = requests.get(url)

cont = res.content
con = json.loads(cont)

for k in con.keys():
    print(k,":",con[k])

