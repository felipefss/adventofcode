import java.io.File

fun buildPointsList(w: List<String>): Wire {
    val points = mutableListOf<Point>()
    val lines = mutableListOf<Line>()
    var x = 0
    var y = 0

    for (p in w) {
        val dist = p.drop(1).toInt()
        val prev = Point(x, y)
        when {
            p.startsWith('R') -> {
                x += dist
                inter.y.add(y)
            }
            p.startsWith('L') -> {
                x -= dist
                inter.y.add(y)
            }
            p.startsWith('U') -> {
                y += dist
                inter.x.add(x)
            }
            p.startsWith('D') -> {
                y -= dist
                inter.x.add(x)
            }
        }
        val current = Point(x, y)
        val newLine = Line(prev, current)
        newLine.addSteps(dist)
        points.add(current)
        lines.add(newLine)
    }
    return Wire(points, lines)
}

fun findIntersection(l1: List<Line>, l2: List<Line>) {
    for (x in inter.x) {
        for (y in inter.y) {
            val line1 = l1.indexOfFirst { it.contains(Point(x, y)) }
            val line2 = l2.indexOfFirst { it.contains(Point(x, y)) }

            if (line1 != -1 && line2 != -1) {
                inter.calcDist(x, y)
                inter.calcSteps(x, y, line1, line2, l1, l2)
            }
        }
    }
}

val inter = Intersection()

fun main() {
    val allWires = mutableListOf<List<String>>()

    File("input.txt").forEachLine { str ->
        val w = str.split(',')
        allWires.add(w)
    }

    val wire1 = buildPointsList(allWires[0])
    val wire2 = buildPointsList(allWires[1])
    findIntersection(wire1.lines, wire2.lines)
    println("Closest intersection at ${inter.crossPoint}")
    println("Distance to central port: ${inter.minDist}")
    println("Fewest combined steps at ${inter.stepsPoint} with ${inter.minSteps} steps")
}