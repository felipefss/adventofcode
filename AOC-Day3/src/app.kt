import java.io.File

fun buildPoints(w: List<String>): MutableList<List<Int>> {
    val wire = mutableListOf<List<Int>>()
    var x = 0
    var y = 0

    for (p in w) {
        val dist = p.drop(1).toInt()
        when {
            p.startsWith('R') -> {
                wire.add(listOf(x + dist, y))
                x += dist
            }
            p.startsWith('L') -> {
                wire.add(listOf(x - dist, y))
                x -= dist
            }
            p.startsWith('U') -> {
                wire.add(listOf(x, y + dist))
                y += dist
            }
            p.startsWith('D') -> {
                wire.add(listOf(x, y - dist))
                y -= dist
            }
        }
    }
    return wire
}

fun findIntersection(w1: List<List<Int>>, w2: List<List<Int>>) {
    val size = if (w1.size > w2.size) w2.size else w1.size
}

fun main() {
    val allWires = mutableListOf<List<String>>()

    File("input.txt").forEachLine { str ->
        val w = str.split(',')
        allWires.add(w)
    }

    val wire1 = buildPoints(allWires[0])
    val wire2 = buildPoints(allWires[1])

    println(wire1)
    println(wire2)
}