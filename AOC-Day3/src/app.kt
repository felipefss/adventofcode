import java.io.File

fun buildPointsList(w: List<String>): MutableList<Point> {
    val wire = mutableListOf<Point>()
    var x = 0
    var y = 0

    for (p in w) {
        val dist = p.drop(1).toInt()
        when {
            p.startsWith('R') -> {
                wire.add(Point(x + dist, y))
                x += dist

            }
            p.startsWith('L') -> {
                wire.add(Point(x - dist, y))
                x -= dist
            }
            p.startsWith('U') -> {
                wire.add(Point(x, y + dist))
                y += dist
            }
            p.startsWith('D') -> {
                wire.add(Point(x, y - dist))
                y -= dist
            }
        }
    }
    return wire
}

fun findIntersection() {

}

fun main() {
    val allWires = mutableListOf<List<String>>()

    File("input.txt").forEachLine { str ->
        val w = str.split(',')
        allWires.add(w)
    }

    println(buildPointsList(allWires[0]))
}