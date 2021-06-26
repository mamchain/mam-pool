#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import json

def run_cmd(cmd):
    info = subprocess.run(cmd, shell=True,stdout=subprocess.PIPE,universal_newlines=True)
    return info.stdout
def get_pool_addr(len):
    cmd = "minemon-cli getforkheight"
    mam_height = run_cmd(cmd).strip("\n")
    cmd = "minemon-cli getblockhash %s" % mam_height
    block_hash = json.loads(run_cmd(cmd))[0]
    pool_addr = []
    for i in range(len):
        cmd = "minemon-cli getblock %s " % block_hash
        ret = json.loads(run_cmd(cmd))
        block_hash = ret["hashPrev"]
        if block_hash == "0000000000000000000000000000000000000000000000000000000000000000":
            break
        cmd = "minemon-cli gettransaction %s" % ret["txmint"]
        ret = json.loads(run_cmd(cmd))
        pool_addr.append(ret["transaction"]["sendto"])
    return mam_height,pool_addr

#exit()
bitcoin_str = ""
with open('./pool_configs/bitcoin.json','r') as f:
    pool_addr0 = []
    pool_addr1 = []
    data = json.load(f)
    pool_addr1 = list(data["daemons"][0]["mam"]["mint_addr"])
    l = data["daemons"][0]["mam"]["len"]
    mam_height, pool_addr = get_pool_addr(l - 1)
    pool_addr = pool_addr[::-1]
    for i in range(len(pool_addr)):
        for obj in data["daemons"][0]["mam"]["mint_addr"]:
            if pool_addr[i] == obj["pool_addr"] and obj not in pool_addr0:
                pool_addr0.append(obj)
                pool_addr1.remove(obj)
                break

    current_addr = pool_addr1[0]
    pool_addr0.append(current_addr)
    pool_addr1.remove(current_addr)
    if len(pool_addr0) >= l:
        obj = pool_addr0[0]
        pool_addr0.remove(obj)
        pool_addr1.append(obj)
    
    data["daemons"][0]["mam"]["mint_addr0"] = pool_addr0
    data["daemons"][0]["mam"]["mint_addr1"] = pool_addr1
    data["daemons"][0]["mam"]["current_addr"] = current_addr
    data["daemons"][0]["mam"]["mam_height"] = mam_height
    bitcoin_str = json.dumps(data,indent=4)

with open('./pool_configs/bitcoin.json','w') as f:
    f.write(bitcoin_str)