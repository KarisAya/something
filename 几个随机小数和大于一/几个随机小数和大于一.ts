// 计算结果 2.7184451 计算耗时 0.2795 秒
const LOOP: number = 10000000;

const start = performance.now();
let n = 0;
for (let _ = 0; _ < LOOP; ++_)
    for (let x = 0.0; x < 1; x += Math.random())
        ++n;
const end = performance.now();

console.log(`计算结果 ${n / LOOP} 计算耗时 ${(end - start) / 1000} 秒`);