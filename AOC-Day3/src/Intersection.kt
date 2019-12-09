import kotlin.math.abs

class Intersection {
    val x = mutableListOf<Int>()
    val y = mutableListOf<Int>()
    var minDist = 9999
    var crossPoint = Point(0, 0)
    var minSteps: Int = 0
    var stepsPoint = Point(0, 0)

    fun calcDist(a: Int, b: Int) {
        if (a == 0 && b == 0) return
        val dist = abs(a) + abs(b)
        if (dist < this.minDist) {
            this.minDist = dist
            crossPoint = Point(a, b)
        }
    }

    fun calcSteps(x: Int, y: Int, index1: Int, index2: Int, l1: List<Line>, l2: List<Line>) {
        if (x == 0 && y == 0) return
        //Line1 steps
        var steps1 = 0
        for (i in 0 until index1) {
            steps1 += l1[i].steps
        }
        steps1 += l1[index1].calcSteps(Point(x, y))

        //Line2 steps
        var steps2 = 0
        for (i in 0 until index2) {
            steps2 += l2[i].steps
        }
        steps2 += l2[index2].calcSteps(Point(x, y))

        val totalSteps = steps1 + steps2
        if (this.minSteps == 0 || totalSteps < this.minSteps) {
            this.minSteps = totalSteps
            stepsPoint = Point(x, y)
        }
    }
}