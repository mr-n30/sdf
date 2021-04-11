#!/usr/bin/env python3
import time
import json
import requests

def crtsh(domain):
    try:
        #print("[+] Requesting crt.sh API...")

        r = requests.get(f"https://crt.sh/?q=%25.{domain}&output=json")

        json_data = json.loads(r.text)

        for domain in json_data:
            print(domain["name_value"])
    except:
        try:
            time.sleep(3)

            r = requests.get(f"https://crt.sh/?q=%25.{domain}&output=json")

            json_data = json.loads(r.text)

            for domain in json_data:
                print(domain["name_value"])
        except:
            try:
                time.sleep(9)

                r = requests.get(f"https://crt.sh/?q=%25.{domain}&output=json")

                json_data = json.loads(r.text)

                for domain in json_data:
                    print(domain["name_value"])
            except:
                pass
