## btc and mam pool
* [Node.js](http://nodejs.org/) v12.22.1
    * For Ubuntu:  
* [npm] (http://nodejs.org/) 6.14.12  
    * For Ubuntu:  
## setup
``` bash
#!/bin/bash
git clone https://github.com/mamchain/pool-mam
cd pool-mam/nomp
npm update
cp -r ../stratum-pool/ ./node_modules/
echo "setup OK!"
npm init.js
```
## Modification content
```bash
find -type f | grep -v '^./.git' | xargs grep mam
```