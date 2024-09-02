// 计算结果 2.7184488 计算耗时 0.162 秒

import java.lang.System.currentTimeMillis
import kotlin.random.Random

const val LOOP = 10000000

fun main() {
    val random = Random(currentTimeMillis())
    val start = currentTimeMillis()
    var n: Long = 0
    repeat(LOOP) {
        var x: Double = 0.0
        while (x < 1) {
            x += random.nextDouble(0.0, 1.0)
            n++
        }

    }
    val end = currentTimeMillis()
    println("计算结果 ${n.toDouble() / LOOP} 计算耗时 ${(end - start).toDouble() / 1000} 秒")
}