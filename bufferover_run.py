#!/usr/bin/env python3
import json
import requests

def bufferover_run(domain):
    try:
        r = requests.get(f"https://dns.bufferover.run/dns?q=.{domain}")

        json_data = json.loads(r.text)

        for x in json_data["FDNS_A"]:
            y = x.split(",")
            print(y[1])
    except:
        pass
