## btc and mam pool
* [Node.js](http://nodejs.org/) v12.22.1
    * For Ubuntu:  
* [npm] (http://nodejs.org/) 6.14.12  
    * For Ubuntu:  
## setup
``` bash
#!/bin/bash
#scp -i /home/shang/mam/ssh/id_rsa_xg -P 25088 newman@59.148.26.46:/home/newman/work/pool/mam-pool/nomp/pool_configs/bitcoin.json /home/shang/mam/mam-pool/nomp/pool_configs

git clone https://github.com/mamchain/pool-mam
cd pool-mam/nomp
npm update
cp -r ../stratum-pool/ ./node_modules/
echo "setup OK!"
./init.sh
```
## Modification content
```bash
find -type f | grep -v '^./.git' | xargs grep mam
```