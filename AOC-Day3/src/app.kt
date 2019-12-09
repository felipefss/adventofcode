import java.io.File

fun buildPointsList(w: List<String>): Wire {
    val points = mutableListOf<Point>()
    val lines = mutableListOf<Line>()
//    val inter = Intersection()
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
        points.add(current)
        lines.add(Line(prev, current))
    }
    return Wire(points, lines)
}

fun findIntersection(l1: List<Line>, l2: List<Line>) {
//    val inter = Intersection()
    for (x in inter.x) {
        for (y in inter.y) {
            val line1 = l1.any {
                it.contains(Point(x, y))
            }
            val line2 = l2.any {
                it.contains(Point(x, y))
            }
            if (line1 && line2) {
                inter.calcDist(x, y)
            }
        }
    }
//    return inter
}

val inter = Intersection()

fun main() {
    val allWires = mutableListOf<List<String>>()

    File("input.txt").forEachLine { str ->
        val w = str.split(',')
        allWires.add(w)
    }

//    val allWires = mutableListOf<List<String>>()
//    allWires.add(listOf("R8","U5","L5","D3"))
//    allWires.add(listOf("U7","R6","D4","L4"))
//    allWires.add(listOf("R75","D30","R83","U83","L12","D49","R71","U7","L72"))
//    allWires.add(listOf("U62","R66","U55","R34","D71","R55","D58","R83"))
//    allWires.add(listOf("R98","U47","R26","D63","R33","U87","L62","D20","R33","U53","R51"))
//    allWires.add(listOf("U98","R91","D20","R16","D67","R40","U7","R15","U6","R7"))

    val wire1 = buildPointsList(allWires[0])
    val wire2 = buildPointsList(allWires[1])
    findIntersection(wire1.lines, wire2.lines)
    println("Closest intersection at ${inter.crossPoint}")
    println("Distance to central port: ${inter.minDist}")
}