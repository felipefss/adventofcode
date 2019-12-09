import kotlin.math.abs

class Intersection {
    val x = mutableListOf<Int>()
    val y = mutableListOf<Int>()
    var minDist: Int = 9999
    var crossPoint = Point(0, 0)

    fun calcDist(a: Int, b: Int) {
        if (a == 0 && b == 0) return
        val dist = abs(a) + abs(b)
        if (dist < this.minDist) {
            this.minDist = dist
            crossPoint = Point(a, b)
        }
    }
}