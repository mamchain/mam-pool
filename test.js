//_this.daemon.instances[0].mam.mint_addr1.push(_this.daemon.instances[0].mam.mint_addr0[0]);
let mint_addr1 = [1,2,3]
mint_addr1.push(4)
mint_addr1.splice(4)
console.log(Math.random(),mint_addr1)
for (let i = 0; i < 200000; i++) {
    let ret = Math.floor(Math.random() * 1);
    if (ret == 1) {
        console.log("err")
    }
}
//console.log( Math.floor(Math.random() * 1));

