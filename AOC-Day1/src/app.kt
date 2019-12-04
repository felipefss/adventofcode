import kotlin.math.*
import java.io.File
import java.lang.Integer.parseInt

/* DAY 1.1 */

fun calcFuel(massList: Collection<Int>): Int {
    var totalFuel: Int = 0
    for (mass in massList) {
        val calc: Double = (mass / 3).toDouble()
        val res: Int = (floor(calc)).toInt() - 2
        totalFuel += res
    }

    return totalFuel
}

fun main() {
    /* DAY 1.1 */
    val modulesMass = mutableListOf<Int>()
    File("input.txt").forEachLine { modulesMass.add(parseInt(it)) }
    println(calcFuel(modulesMass))  // Result: 3291356
}