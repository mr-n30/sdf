#!/usr/bin/env python3
import sys
import json
import yaml
import argparse
import requests
from crtsh import *
from bufferover_run import *
from securitytrails import *

# Arguments
parser = argparse.ArgumentParser(description="Accepts domains from stdin and finds subdomains for each domain")
parser.add_argument("-c", "--config", required=True, help="Path to your config.yaml")

args = parser.parse_args()
yaml_config = args.config

# Read domains from stdin
try:
    domain_list = []
    for line in sys.stdin:
        domain_list.append(line)
except KeyboardInterrupt as e:
    print("\n")
    sys.exit(1)

def pull_subs(domain):
    try:
        with open(yaml_config, 'r') as f:
            yaml_data = yaml.safe_load(f)
        api_key = yaml_data["securitytrails"][0]
        securitytrails(domain, api_key)

        # crt.sh
        crtsh(domain)

        # bufferover.run
        bufferover_run(domain)
    except Exception as e:
        print(f"[!] ERROR in: pull_subs: {e}")
        sys.exit(2)

if __name__ == "__main__":
    for domain in domain_list:
        pull_subs(domain.strip())

