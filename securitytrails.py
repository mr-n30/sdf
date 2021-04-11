#!/usr/bin/env python3
import json
import requests

def securitytrails(domain, api_key):
    try:
        #print("[+] Requesting SecurityTrails API...")

        headers = {
            "Accept": "application/json",
            "apikey": api_key
        }

        url = f"https://api.securitytrails.com/v1/domain/{domain}/subdomains?children_only=false"
        r = requests.get(url, headers=headers)

        json_dict = json.loads(r.text)

        json_list = json_dict["subdomains"]

        for subdomain in json_list:
            print(f"{subdomain}.{domain}")
    except Exception as e:
        print(f"[!] ERROR in: security_trails(): {e}")
        pass
