import kotlin.math.*
import java.io.File
import java.lang.Integer.parseInt

/* Part 1 */

fun calcFuel(massList: Collection<Int>): Int {
    var totalFuel: Int = 0
    for (mass in massList) {
//        val calc: Double = (mass / 3).toDouble()
//        val res: Int = (floor(calc)).toInt() - 2
//        totalFuel += res

        // Part 2
        totalFuel += getTotalModuleFuel(mass)
    }

    return totalFuel
}

/* Part 2 */
fun getTotalModuleFuel(mass: Int): Int {
    val calc: Double = (mass / 3).toDouble()
    val res: Int = (floor(calc)).toInt() - 2

    return if (res > 0) res + getTotalModuleFuel(res) else 0
}

fun main() {
    /* Part 1 */
    val modulesMass = mutableListOf<Int>()
    File("input.txt").forEachLine { modulesMass.add(parseInt(it)) }
//    println(calcFuel(modulesMass))  // Result: 3291356

    /* Part 2 */
    println(calcFuel(modulesMass))
}