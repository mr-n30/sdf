#!/usr/bin/env python3
import sys
import json
import yaml
import requests
from crtsh import *
from bufferover_run import *
from securitytrails import *

domain_list = sys.argv[1]
yaml_config = sys.argv[2]

def pull_subs(domain):
    try:
        with open(yaml_config, 'r') as f:
            yaml_data = yaml.safe_load(f)
        api_key = yaml_data["securitytrails"][0]
        print(f"[DEBUG] YOUR SECURITY TRAILS API KEY IS {api_key}")
        securitytrails(domain, api_key)

        # crt.sh
        crtsh(domain)

        # bufferover.run
        bufferover_run(domain)
    except Exception as e:
        print(f"[!] ERROR in: pull_subs: {e}")
        sys.exit(2)

if __name__ == "__main__":
    # domain list
    with open(domain_list, "r") as f:
        domains = f.readlines()

    for domain in domains:
        #print(f"{domain.strip()}")
        pull_subs(domain.strip())
