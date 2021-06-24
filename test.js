

a = [{a:1},{a:2},{a:3},{a:4},{a:5}]
b = []

b_l = 3
// 模拟初始化
b.push({a:2});
b.push({a:4});

for (let i = 0; i < b.length; i++) {
    for (let j = 0; j < a.length; j++) {
        if (b[i].a == a[j].a) {
            a.splice(j,1);
            break;
        }
    }
}

console.log(a)
console.log(b)
console.log("---------------------")

for (let i = 0; i < 10; i++) {
    const r = Math.floor(Math.random() * a.length);
    b.push(a[r]);

    if (b.length > b_l) {
        a.push(b[0]);
        b.splice(0,1);
    }
    a.splice(r,1);
    console.log("OK",b);
}