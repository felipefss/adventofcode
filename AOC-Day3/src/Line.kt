import kotlin.math.abs

class Line constructor(private val start: Point, private val end: Point) {
    var steps = 0

    fun addSteps(value: Int) {
        this.steps += value
    }

    fun calcSteps(p: Point) = when {
        p.x != this.start.x /*|| p.x != this.end.x*/ -> abs(this.start.x - p.x)
        p.y != this.start.y /*|| p.y != this.end.y*/ -> abs(this.start.y - p.y)
        else -> 0
    }

    override fun toString(): String {
        return "$start -> $end"
    }

    fun contains(p: Point): Boolean {
        val x = p.x
        val y = p.y

        val resX = when {
            x >= start.x && x <= end.x -> true
            x * (-1) >= start.x * (-1) && x * (-1) < end.x * (-1) -> true
            else -> false
        }
        val resY = when {
            y >= start.y && y <= end.y -> true
            y * (-1) >= start.y * (-1) && y * (-1) < end.y * (-1) -> true
            else -> false
        }
        return resX && resY
    }
}