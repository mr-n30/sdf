#!/usr/bin/env python3
import time
import json
import requests

def crtsh(d):
    try:
        r = requests.get(f"https://crt.sh/?q=%25.{d}&output=json")

        json_data = json.loads(r.text)

        for domain in json_data:
            if '*' not in domain["name_value"]:
                if f".{d}" in domain["name_value"]:
                    print(f"{domain['name_value'].lower()}")
    except:
        try:
            # Wait for 30 sec due to rate limit
            time.sleep(30)

            r = requests.get(f"https://crt.sh/?q=%25.{d}&output=json")

            json_data = json.loads(r.text)

            for domain in json_data:
                if '*' not in domain["name_value"]:
                    if f".{d}" in domain["name_value"]:
                        print(f"{domain['name_value'].lower()}")
        except:
            pass
